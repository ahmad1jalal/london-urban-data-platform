# importing libraries...
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import logging

logging.basicConfig(
    filename = "logs/pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"

)

def load_traffic_data(df):
    
        try:
            logging.info("starting traffic data load")
            
            df = pd.read_csv(df)
            # setup the db
            conn = psycopg2.connect(
                dbname = "london_data",
                user = "postgres",
                password = "polo00",
                host = "localhost",
                port = "5432"

            )
            cur = conn.cursor()

            # insert into dim_location

            dim_location = df[[
                "road_name",
                "region_name",
                "local_authority_name",
                "latitude",
                "longitude"
            ]].drop_duplicates().values.tolist()

            location_query = """
INSERT INTO dim_location (road_name, region_name, local_authority_name, latitude, longitude)
VALUES %s
ON CONFLICT (road_name, region_name, local_authority_name, latitude, longitude)
DO NOTHING;
"""
            execute_values(cur,location_query,dim_location)


            # fectch location ids
            cur.execute("SELECT location_id,road_name,latitude,longitude FROM dim_location")
            location_map = {
                (row[1],row[2],row[3]) : row[0]
                for row in cur.fetchall()
            }
            fact_data = [
                (
                    location_map[(row["road_name"], row["latitude"], row["longitude"])],
                    row["datetime"],
                    row["cars_and_taxis"],
                    row["buses_and_coaches"],
                    row["all_hgvs"],
                    row["all_motor_vehicles"]
                )
                for _, row in df.iterrows()
            ]
            fact_query = """
            INSERT INTO fact_traffic (
                location_id, datetime, cars, buses, hgvs, total_vehicles
            )
            VALUES %s
            """

            execute_values(cur, fact_query, fact_data)

            conn.commit()
            cur.close()
            conn.close()

            logging.info(f"{len(fact_data)} rows loaded into fact_traffic")
        except Exception as e:
            logging.error(f"Error loading traffic data {e}")    
            raise 


