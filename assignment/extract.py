import pandas as pd

def extract_orders(engine):
    query = "SELECT * FROM orders_raw"
    with engine.raw_connection() as conn:
        return pd.read_sql(query, conn)

