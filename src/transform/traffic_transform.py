import pandas as pd
import logging
from datetime import datetime
# logging setup

logging.basicConfig(
    filename = "logs/pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s -%(message)s"
)

# transforming the data...
def transform_data_traffic(df):
    try :
        logging.info("Transforming Traffic Data")

        # loading data-set
        df = pd.read_csv(df)

         # standardize the column names
        df.columns = [col.strip().lower() for col in df.columns]

         # dropping the duplicates
        df = df.drop_duplicates()

        # selecting the useful columns
        cols_to_keep = [
        "count_date",
        "hour",
        "road_name",
        "region_name",
        "local_authority_name",
        "latitude",
        "longitude",
        "cars_and_taxis",
        "buses_and_coaches",
        "all_hgvs",
        "all_motor_vehicles"
    ]

        df = df[cols_to_keep]

        # converting the datatime
        df["count_date"] = pd.to_datetime(df["count_date"],errors = "coerce")

        # create unified datetime
        df["datetime"] = df["count_date"] + pd.to_timedelta(df["hour"],unit = "h")

        logging.info("Traffic transform successfully")

        return df
    except Exception as e:
        logging.error(f"Error during transformation : {e}")
        raise

def save_transform(df):
    try :
        file_name = f"data/processed/traffic_{datetime.now().date()}.csv"
        df.to_csv(file_name,index = False)
        logging.info("Prcessed data saved successfully")
    except Exception as e:
        logging.error(f"Error occured saving processed data : {e}")
        raise

