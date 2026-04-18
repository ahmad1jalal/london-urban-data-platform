import pandas as pd
import logging
from datetime import datetime
# logging setup

logging.basicConfig(
    filename = "logs/pipeline.log",
    level = "logging.INFO",
    format = "%(asctime)s - %(levelname)s -%(message)s"
)

# transforming the data...
def tranform_traffic(df):
    logging.info("Transforming Traffic Data")

    # loading data-set
    df = pd.read_csv(df)

    # standardize the column names
    df.columns = []
