# 🌍 London Urban Data Platform
This project demonstrates real-world data engineering practices including ETL pipelines, data validation, and dimensional data modeling.

## 📌 Project Overview

This project is a **production-style data engineering pipeline** that collects, processes, and analyzes urban data in London, focusing on **air quality and traffic data integration**.
The system evolves into a mini data warehouse using dimensional modeling (fact and dimension tables).
The goal is to simulate a real-world data engineering system by building an end-to-end pipeline:

Extract → Transform → Validate → Load → Data Warehouse → Analyze

## 🚀 Tech Stack

* Python (pandas, requests)
* PostgreSQL
* SQL
* Git & GitHub
* Logging (Python logging module)

---

## 🧱 Project Architecture

```
Data Source (CSV/API)
        ↓
Extract (Python)
        ↓
Raw Data Storage (data/raw)
        ↓
Transform (Cleaning & Processing)
        ↓
Processed Data (data/processed)
        ↓
Load (PostgreSQL)
        ↓
SQL Analysis
```

---
## 🏗️ Data Warehouse Design

The project uses a dimensional model:

### Dimension Table
**dim_location**
- road_name
- region_name
- latitude, longitude

### Fact Tables
**fact_traffic**
- datetime
- traffic counts (cars, buses, etc.)

**air_quality (planned upgrade → fact_air_quality)**
- pollutant levels by site and time

This structure improves scalability, query performance, and data consistency.

## 📂 Project Structure

```
london-urban-data-platform/
│
├── data/
│   ├── raw/              # Raw extracted data
│   ├── processed/        # Cleaned & transformed data
│
├── src/
│   ├── extract/          # Data extraction scripts
│   ├── transform/        # Data cleaning & transformation
│   ├── load/             # Load data into PostgreSQL
│
├── sql/                  # SQL analysis queries
├── logs/                 # Pipeline logs
├── notebooks/            # Exploration (optional)
├── config/               # Config files
│
├── main.py               # Pipeline entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Pipeline Stages

### 1️⃣ Extract

* Data is fetched from London air quality datasets
* Stored in `data/raw/`
* Logging implemented for monitoring

---

### 2️⃣ Transform

* Cleaned missing values
* Standardized column names
* Converted datetime fields
* Removed duplicates and invalid values
* Aggregated and structured data

---
### 3️⃣ Validate
- Ensures data quality before loading
- Checks for null values and invalid data
- Prevents bad data entering the system
  
### 4️⃣ Load
- Data loaded into PostgreSQL warehouse
- Uses dimension and fact tables
- Implements surrogate keys (location_id)
- Bulk insert with conflict handling

---

## 🔥 Future Improvements

* Integrate air quality into warehouse (fact_air_quality)
* Build analytical layer combining traffic + pollution
* Add dashboard (Streamlit / Power BI)
* Automate pipeline (Airflow)
* Add data quality monitoring alerts

#### 🔹 Top Polluted Sites

```sql
SELECT site, AVG(value) AS avg_pollution
FROM air_quality
GROUP BY site
ORDER BY avg_pollution DESC
LIMIT 10;
```

#### 🔹 Pollution Trend Over Time

```sql
SELECT DATE(readingdatetime) AS date, AVG(value) AS avg_pollution
FROM air_quality
GROUP BY date
ORDER BY date;
```

#### 🔹 Peak Pollution Hours

```sql
SELECT EXTRACT(HOUR FROM readingdatetime) AS hour,
       AVG(value) AS avg_pollution
FROM air_quality
GROUP BY hour
ORDER BY avg_pollution DESC;
```

---

## 📊 Key Insights

* Pollution levels vary significantly by location (site)
* Peak pollution occurs during specific hours (likely traffic-related)
* Different pollutants (species) show different patterns

---

## 🧠 What I Learned

* Building end-to-end data pipelines
* Data cleaning and transformation techniques
* PostgreSQL integration and optimization
* Writing efficient SQL queries
* Handling real-world messy data

---

## 🔥 Future Improvements

* Add multiple datasets (transport, population)
* Automate pipeline using scheduling (cron/Airflow)
* Build dashboard (Power BI / Tableau)
* Implement data warehouse (fact/dimension tables)

---

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repo-url>
cd london-urban-data-platform
```

2. Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run pipeline:

```
python main.py
```

---

## 👤 Author

Ahmad Jalal

---

## 📌 Note

This project is part of a hands-on journey to becoming a **Data Engineer**, focusing on real-world datasets and production-style practices.
