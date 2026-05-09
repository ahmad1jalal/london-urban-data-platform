import logging

# import modules
# from src.extract.air_quality_extract import extract_air_quality
# from src.extract.air_quality_defra import extract_air_quality_def
# from data.raw.save_raw_data import save_raw
# from src.transform.air_quality_transform import transform_air_quality_data,save_processed_data
from src.load.air_quality import load_data
# from src.extract.traffic_raw_extract import extract_traffic_raw,save_raw_traffic_data
# from src.transform.traffic_transform import transform_data_traffic,save_transform
# from src.load.load_traffic import load_traffic_data
# from src.utls.validate import validate_traffic_data

logging.basicConfig(
    filename = "logs/pipeline.log",
    level = logging.INFO,
    format = "%(asctime)s -%(levelname)s - %(message)s"
)

def run_pipeline():
    try : 
        logging.info("===== Pipeline Started =====")
        # df = extract_air_quality()
        # save_raw(df)
        # df = extract_air_quality_def()
        # save_raw(df)
        # dt_transformed = transform_air_quality_data("data/raw/air_quality_2026-03-30.csv")
        # save_processed_data(dt_transformed)
        load_data("./data/processed/air_quality_2026-04-01.csv")
        # df = extract_traffic_raw()
        # save_raw_traffic_data(df)
        # dt_traffic_transform = transform_data_traffic("./data/raw/traffic_2026-04-05.csv")
        # save_transform(dt_traffic_transform)
        # load_traffic_data("./data/processed/traffic_2026-04-24.csv")
        # validate_traffic_data("./data/processed/traffic_2026-04-24.csv")

        logging.info("=== Pipeline completed successfully ===")


    except Exception as e:
        logging.error(f"Pipeline Failed : {e}")
        raise    


if __name__  == "__main__":
    run_pipeline()
