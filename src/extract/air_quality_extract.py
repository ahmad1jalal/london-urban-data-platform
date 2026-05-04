import requests
import pandas as pd
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_air_quality():
    try:
        logging.info("Extracting air quality data from OpenAQ API (v3)")

        url = "https://api.openaq.org/v3/locations"

        params = {
    "country": "GB",
    "limit": 100
}

        headers = {
    "Accept": "application/json",
    "X-API-Key": "1ba817b67617c083ffea376ac7d2f5390146b83648825f75cadfaf355816e007"   # <-- add this
        }

        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        json_data = response.json()

        # v3 uses 'results' OR 'data' depending on endpoint version
        data = json_data.get("results") or json_data.get("data")

        if not data:
            raise ValueError("No data found in API response")

        records = []

        for item in data:
            coords = item.get("coordinates") or {}

            records.append({
                "site": item.get("name"),
                "city": item.get("city"),
                "country": item.get("country"),
                "latitude": coords.get("latitude"),
                "longitude": coords.get("longitude"),
                "count": item.get("counts", {}).get("measurements")
            })

        df = pd.DataFrame(records)

        logging.info(f"Extracted {len(df)} air quality locations")

        return df

    except Exception as e:
        logging.exception(f"Error extracting air quality: {e}")
        raise