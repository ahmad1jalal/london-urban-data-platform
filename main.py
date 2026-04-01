from src.extract.air_quality_extract import extract_air_quality_data
from data.raw.save_raw_data import save_raw
from src.transform.air_quality_transform import transform_air_quality_data,save_processed_data



def run_pipeline():
    # df = extract_air_quality_data()
    # save_raw(df)
    dt_transformed = transform_air_quality_data("data/raw/air_quality_2026-03-30.csv")
    save_processed_data(dt_transformed)


if __name__  == "__main__":
    run_pipeline()
