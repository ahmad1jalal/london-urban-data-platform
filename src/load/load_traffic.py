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
            # insert into dim_location
            location_data = [
                (row["road_name"], "road")
                for _, row in df[["road_name"]].drop_duplicates().iterrows()
                ]

            location_query = """
            INSERT INTO dim_location(location_name, location_type)
            VALUES %s
            ON CONFLICT (location_name, location_type) DO NOTHING
            """

            execute_values(cur, location_query, location_data)

            # fetch mapping
            cur.execute("""
                SELECT location_id, location_name
                FROM dim_location
                WHERE location_type = 'road'
                """)

            location_map = {row[1]: row[0] for row in cur.fetchall()}

            # build fact
            fact_data = [
                (
                location_map[row["road_name"]],
                row["count_date"],   # IMPORTANT FIX (not datetime)
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


