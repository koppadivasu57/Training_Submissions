import pandas as pd
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract():
    logging.info("Extract step started")
    data = {
        "Product": ["Laptop", "Tablet", "Phone"],
        "Sales": [1000, 500, 800]
    }
    return pd.DataFrame(data)

def transform(df):
    logging.info("Transform step started")
    df["Sales_With_Tax"] = df["Sales"] * 1.08
    return df

def load(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sales_output_{timestamp}.csv"
    df.to_csv(filename, index=False)
    logging.info(f"Data loaded into {filename}")

def etl_pipeline():
    logging.info("ETL pipeline started")
    df = extract()
    df = transform(df)
    load(df)
    logging.info("ETL pipeline completed")

# Run ETL
etl_pipeline()
print("ETL process completed successfully!")
