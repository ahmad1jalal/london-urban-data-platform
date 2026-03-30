import pandas as pd
import logging

# setup logging
logging.basicCongif(filename = "logs/pipeline.log",
                    level = logging.INFO,
                    message = "%(asctime)s - %(levelname)s - %(message)")

def extract_air_quality_date():
    try:
        loggign.info("Extracting air quality data...")

        url = "https://www.londonair.org.uk/london/asp/downloadsite.asp?site=MY1&species1=NO2m&species2=&species3=&species4=&species5=&species6=&start=01-Jan-2023&end=31-Dec-2023&res=hourly&Submit=Download+Data"

        # data-set
        df = pd.read_csv(url)

        logging.info(f"Data extracted successfully. Rows : {len(df)}")

        return df
    except Exception as e:
        logging.info(f"Error during data extraction {e}")
        raise
    

    