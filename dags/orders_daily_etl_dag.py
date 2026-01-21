from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append("C:\Users\antar\Desktop\sql_python")

from assignment.daily_etl import run_pipeline

default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="daily_orders_etl",
    default_args=default_args,
    description="Daily ETL with data quality checks and reconciliation",
    schedule_interval="*/2 * * * *",  
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["etl", "data-quality"],
) as dag:

    run_etl = PythonOperator(
        task_id="run_daily_etl_pipeline",
        python_callable=run_pipeline
    )

    run_etl
