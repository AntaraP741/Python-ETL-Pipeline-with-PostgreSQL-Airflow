def transform_orders(df):
    df = df.drop_duplicates(subset=["order_id"])
    df = df[df["amount"] > 0]

    def classify(amount):
        if amount < 1000:
            return "LOW"
        elif amount <= 5000:
            return "MEDIUM"
        return "HIGH"

    df["order_value_category"] = df["amount"].apply(classify)
    return df
