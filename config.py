PROJECT_ID = "your-gcp-project-id"

BUCKET_NAME = "your-customer360-bucket"
TEMP_BUCKET_NAME = "your-temp-bucket"

RAW_PATH = f"gs://{BUCKET_NAME}/raw"
CURATED_PATH = f"gs://{BUCKET_NAME}/curated"
REJECTED_PATH = f"gs://{BUCKET_NAME}/rejected"

BIGQUERY_DATASET = "customer360"

CUSTOMER_TABLE = "dim_customer"
ORDER_TABLE = "fact_orders"
PAYMENT_TABLE = "fact_payments"
CUSTOMER_360_TABLE = "customer_360"
