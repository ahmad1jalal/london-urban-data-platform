import pandas as pd
import logging 

logging.basicConfig(
    filename = "logs/pipeline.log",
    level = logging.INFO,
    format  = "%(asctime)s - %(level)s - %(message)s"
)
def validate_traffic_data(df):
    try : 
        logging.info("Starting traffic data validation")

        # reading data-frame
        df = pd.read_csv(df)
        # checking empy data-frame
        if df.empty:
            raise ValueError("DataFrame is empty")
        
        # required columns
        req_columns = [
        "datetime",
        "road_name",
        "all_motor_vehicles"
    ]
        for col in req_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required columns : {col}")
        
         # checking nulls in critical fields:
        if df["datetime"].isnull().sum() > 0:
            raise ValueError("Null values in datetime")
    
        if df["road_name"].isnull().sum() > 0:
            raise ValueError("null values in road_name")
    
        # negative values in motor-vehicles
        if (df["all_motor_vehicles"] < 0).any():
            raise ValueError("Negative Traffic Values Found")
    
        logging.info("Traffic Data validation pass")

    except Exception as e:
        logging.error(f"Validation error : {e}")
        raise

