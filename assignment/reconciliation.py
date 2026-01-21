import logging
import hashlib

def checksum(df):
    data = df["amount"].astype(str).str.cat()
    return hashlib.md5(data.encode()).hexdigest()

def reconcile(conn, raw_df, clean_df):
    raw_count = len(raw_df)
    clean_count = len(clean_df)

    raw_checksum = checksum(raw_df)
    clean_checksum = checksum(clean_df)

    logging.info(f"Row Count - Raw: {raw_count}, Clean: {clean_count}")
    logging.info(f"Checksum - Raw: {raw_checksum}, Clean: {clean_checksum}")