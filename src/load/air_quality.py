import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(file_path):
    try:
        logging.info("Loading air quality data into PostgreSQL")

        df = pd.read_csv(file_path)

        conn = psycopg2.connect(
            dbname="london_data",
            user="postgres",
            password="polo00",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # -------------------------
        # 1. Insert into dim_location
        # -------------------------
        # insert into dim_location
        location_data = [
         (row["site"], "site")
        for _, row in df[["site"]].drop_duplicates().iterrows()
        ]

        query = """
        INSERT INTO dim_location(location_name, location_type)
        VALUES %s
        ON CONFLICT (location_name, location_type) DO NOTHING
        """

        execute_values(cur, query, location_data)

        # fetch mapping
        cur.execute("""
            SELECT location_id, location_name
            FROM dim_location
            WHERE location_type = 'site'
            """)

        location_map = {row[1]: row[0] for row in cur.fetchall()}

        # build fact
        fact_data = [
         (
        location_map[row["site"]],
        row["readingdatetime"],
        row["species"],
        row["value"],
        row["units"]
    )
        for _, row in df.iterrows()
]

        fact_query = """
        INSERT INTO fact_air_quality(
            location_id, datetime, species, value, units
        )
        VALUES %s
        """

        execute_values(cur, fact_query, fact_data)

        conn.commit()
        cur.close()
        conn.close()

        logging.info(f"{len(fact_data)} rows loaded into fact_air_quality")

    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise