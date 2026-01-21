import logging

def data_quality_checks(df):
    errors = []

    if df["order_id"].isnull().any():
        errors.append("NULL order_id found")

    if df["amount"].isnull().any():
        errors.append("NULL amount found")

    if (df["amount"] <= 0).any():
        errors.append("Non-positive amount found")

    if errors:
        for e in errors:
            logging.error(e)
        raise Exception("Data quality checks failed")
