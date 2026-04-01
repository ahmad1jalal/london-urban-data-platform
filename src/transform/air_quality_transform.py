import pandas as pd
import logging
from datetime import datetime

# logging setup
logging.basicConfig(filename = "logs/pipeline.log",
                    level = logging.INFO,
                    format="%(asctime)s - %(levelname)s -%(message)s")

def transform_air_quality_data(df):

    try:
        logging.info("Starting data transformation")

        # loading the data...
        df = pd.read_csv(df)
        # standardize the column names
        df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]

        # dropping the missing values
        df = df.dropna()

        # changing the datetime column type
        df["readingdatetime"]  = pd.to_datetime(df["readingdatetime"],dayfirst=True)

        # extracing the new feature
        df["month"] = df["readingdatetime"].dt.month

        # aggregate the value on monthly basis
        df.groupby("month")["value"].mean()

        logging.info("Transformation completed successfully")
    
        return df
    except Exception as e:
        logging.error(f"Error occur during transformation : {e}")
        raise


def save_processed_data(df):
    try:
        file_name = f"data/processed/air_quality_{datetime.now().date()}.csv"
        df.to_csv(file_name,index = False)
        logging.info("Prcessed data saved successfully")
    except Exception as e:
        logging.error(f"Error occured saving processed data : {e}")
        raise
    

