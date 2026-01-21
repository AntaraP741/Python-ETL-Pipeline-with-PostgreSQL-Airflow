# Python ETL Pipeline with PostgreSQL & Airflow

## Overview

This repository contains a **modular Python ETL pipeline** that connects to a **PostgreSQL database**, performs **data extraction, transformation, loading (ETL)**, executes **reconciliation and data quality checks**, and is **scheduled using Apache Airflow**.

The project demonstrates **real-world data engineering practices**, including SQL execution from Python, modular code design, automation, and validation.

---

## Architecture

```
PostgreSQL (orders_raw)
        ↓
   Extract (SQLAlchemy)
        ↓
   Transform (Pandas)
        ↓
 Data Quality Checks
        ↓
   Load (orders_clean)
        ↓
 Reconciliation & Logging
        ↓
     Airflow Scheduler
```

---

## Project Structure

```
assignment/
│
├── db_config.py          # SQLAlchemy engine configuration
├── extract.py            # Data extraction from PostgreSQL
├── transform.py          # Data transformations
├── load.py               # Load data into target table
├── data_quality.py       # Data quality validations
├── reconciliation.py     # Row count & checksum validation
├── daily_etl.py          # ETL orchestration
│
└── dags/
    └── orders_daily_etl_dag.py   # Airflow DAG
```

---

## Technologies Used

* **Python 3**
* **PostgreSQL**
* **Pandas**
* **SQLAlchemy**
* **Apache Airflow**
* **Logging**

---

## Database Tables

### Source Table: `orders_raw`

```sql
order_id INT
customer_name VARCHAR
product VARCHAR
amount DECIMAL
order_date DATE
created_at TIMESTAMP
```

### Target Table: `orders_clean`

```sql
order_id INT
customer_name VARCHAR
product VARCHAR
amount DECIMAL
order_date DATE
created_at TIMESTAMP
order_value_category VARCHAR
```

---

## How the Pipeline Works

1. **Extract**

   * Reads data from `orders_raw` using SQLAlchemy
2. **Transform**

   * Removes duplicates
   * Filters invalid amounts
   * Adds `order_value_category` (LOW / MEDIUM / HIGH)
3. **Data Quality Checks**

   * No NULLs in critical fields
   * No non-positive amounts
4. **Load**

   * Writes clean data to `orders_clean`
5. **Reconciliation**

   * Compares row counts
   * Computes checksums
6. **Scheduling**

   * Airflow runs the pipeline automatically every 2 minutes

---

## How to Run the Project

### 1️ Install Dependencies

```bash
pip install pandas sqlalchemy psycopg2-binary apache-airflow
```

---

### 2️ Configure Database

Update credentials in `db_config.py`:

```python
DB_CONFIG = {
    "host": <host_name>,
    "database": <db_name>,
    "user": <username>,
    "password": <password>,
    "port": 5432
}
```

---

### 3️ Insert Sample Data

```sql
INSERT INTO orders_raw VALUES
(1, 'Alice', 'Laptop', 45000, '2026-01-20', NOW()),
(2, 'Bob', 'Mouse', 500, '2026-01-20', NOW());
```

---

### 4️ Run Manually (Testing)

```bash
python daily_etl.py
```

---

### 5️ Run via Airflow (Recommended)

Start Airflow:

```bash
airflow standalone
```

Open browser:

```
http://localhost:8080
```

Enable and trigger:

```
daily_orders_etl
```

---

##  Airflow Scheduling

The DAG is scheduled to run **every 2 minutes**:

```python
schedule_interval="*/2 * * * *"
```

---

##  Logging & Monitoring

* Execution logs stored in `daily_etl.log`
* Airflow UI provides:

  * Task status
  * Retry handling
  * Failure diagnostics




Just say what you want next.
