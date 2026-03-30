from src.extract.air_quality_extract import extract_air_quality_data
from data.raw.save_raw_data import save_raw


def run_pipeline():
    df = extract_air_quality_data()
    save_raw(df)

if __name__  == "__main__":
    run_pipeline()
