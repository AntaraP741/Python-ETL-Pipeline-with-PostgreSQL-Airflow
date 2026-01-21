def load_orders(engine, df):
    with engine.raw_connection() as conn:
        df.to_sql(
            "orders_clean",
            conn,
            if_exists="replace",
            index=False
        )
