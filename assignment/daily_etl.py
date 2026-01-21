import logging
from extract import extract_orders
from transform import transform_orders
from load import load_orders
from reconciliation import reconcile
from data_quality import data_quality_checks
from db_config import get_engine

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("ETL job started")

    engine = get_engine()

    raw_df = extract_orders(engine)
    clean_df = transform_orders(raw_df)

    data_quality_checks(clean_df)
    load_orders(engine, clean_df)
    reconcile(raw_df, clean_df)

    logging.info("ETL job completed successfully")

if __name__ == "__main__":
    run_pipeline()
