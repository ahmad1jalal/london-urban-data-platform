import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import logging
# setup the logging
logging.basicConfig(filename="logs/pipeline.log",
                    level = logging.INFO,
                    format = "%(asctime)s - %(levelname)s -%(message)s")

def load_data(df):
    try : 
        logging.info("Data loading into PostgeSQL")
        df = pd.read_csv(df)
        # let's connect the postgres
        conn = psycopg2.connect(
            dbname = "london_data",
            user = "postgres",
            password = "polo00",
            host = "localhost",
            port = "5432"
        )
        cur = conn.cursor()

        # let's make the data point
        data = ([row["site"],
                row["species"],
                row["readingdatetime"],
                row["value"],
                row["units"],
                row["provisional_or_ratified"],
                row["month"],]
                for _,row in df.iterrows())

        # let's make a query
        query = """
        INSERT INTO air_quality(site,species,readingdatetime,value,units,provisional_or_ratified,month) VALUES %s
        """

        # let's execute the query
        execute_values(cur,query,data)
        conn.commit()
        cur.close()
        conn.close()
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Error loading data {e}")
        raise
