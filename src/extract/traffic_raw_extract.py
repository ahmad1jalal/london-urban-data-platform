import pandas as pd
import logging
import os
from datetime import datetime
# setup logging
logging.basicConfig(filename="logs/pipeline.log",
                    level = logging.INFO,
                    format = "%(asctime)s - %(levelname)s - %(message)s")

def extract_traffic_raw():
    try:
        logging.info("Extracting Traffic Raw data...")

        url = "https://storage.googleapis.com/dft-statistics/road-traffic/downloads/rawcount/local_authority_id/dft_rawcount_local_authority_id_174.csv"

        # reading data-set

        df = pd.read_csv(url)

        logging.info("Traffic Raw data extracted successfully")

        return df
    
    except Exception as e:
        logging.error(f"Error occur during extraction :{e}")
        raise

def save_raw_traffic_data(df):
    try:
        os.makedir("data/raw",exist_ok = True)
        file_name = f"data/raw/traffic_{datetime.now().date()}.csv"
        df.to_csv(file_name,index=False)
        logging.info("Traffic Raw data Saved Successfully")

    except Exception as e:
        logging.error(f"Error occur during Processing data  :{e}")
        raise