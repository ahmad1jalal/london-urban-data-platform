import requests
import pandas as pd
import logging

def extract_air_quality_measurements():
    try:
        logging.info("Extracting real air quality measurements")

        # Example site code (you will loop later)
        url = "https://api.erg.ic.ac.uk/AirQuality/Data/Site/SiteCode=MY1/Json"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        records = []

        # structure depends on pollutant series
        measurements = data.get("AirQualityData", {}).get("Pollutant", [])

        for m in measurements:
            records.append({
                "site": "MY1",
                "datetime": m.get("@MeasurementDateGMT"),
                "species": m.get("@Species"),
                "value": m.get("@Value"),
                "units": m.get("@Units")
            })

        df = pd.DataFrame(records)

        logging.info(f"Extracted {len(df)} measurement rows")

        return df

    except Exception as e:
        logging.error(f"Error: {e}")
        raise