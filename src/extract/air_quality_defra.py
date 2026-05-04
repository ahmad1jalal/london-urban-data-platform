import requests
import pandas as pd
import logging

def extract_air_quality_def():
    try:
        logging.info("Extracting air quality from DEFRA API")

        url = "https://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName=London/Json"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        records = []

        stations = (
            data.get("HourlyAirQualityIndex", {})
                .get("LocalAuthority", [])
        )

        for area in stations:
            sites = area.get("Site")

            # Case 1: missing
            if not sites:
                continue

            # Case 2: single dict → convert to list
            if isinstance(sites, dict):
                sites = [sites]

            # Case 3: bad type
            if isinstance(sites, str):
                logging.warning(f"Unexpected string site: {sites}")
                continue

            for site in sites:
                if not isinstance(site, dict):
                    logging.warning(f"Skipping invalid site type: {type(site)}")
                    continue

                records.append({
                    "site": site.get("@SiteName"),
                    "value": site.get("@AirQualityIndex"),
                    "datetime": site.get("@MeasurementDateUTC")
                })

        df = pd.DataFrame(records)

        logging.info(f"Extracted {len(df)} rows from DEFRA")

        return df

    except Exception as e:
        logging.exception(f"Error extracting DEFRA data: {e}")
        raise