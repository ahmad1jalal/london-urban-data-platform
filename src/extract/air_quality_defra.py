import requests
import pandas as pd
import logging

def extract_air_quality_def():
    try:
        logging.info("Extracting corrected DEFRA data")

        url = "https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName=London/Json"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        records = []

        sites = data["Sites"]["Site"]

        if isinstance(sites, dict):
            sites = [sites]

        for site in sites:
            records.append({
                "site": site.get("@SiteName"),
                "latitude": site.get("@Latitude"),
                "longitude": site.get("@Longitude"),
                "value": None,        # IMPORTANT: no pollution here
                "datetime": None,
                "species": None,
                "units": None
            })

        df = pd.DataFrame(records)

        logging.info(f"Extracted {len(df)} location records")

        return df

    except Exception as e:
        logging.error(f"Error: {e}")
        raise