# Customer 360 PySpark Data Engineering Project

End-to-end Data Engineering project using PySpark, Google Cloud Storage (GCS), Dataproc, BigQuery and Airflow/Cloud Composer.

## Architecture

Source CSV files -> GCS Raw -> PySpark/Dataproc -> Data Quality -> Deduplication -> Transformations -> BigQuery

## Project structure

```text
customer-360-pyspark/
├── data/
│   ├── customers/customers.csv
│   ├── orders/orders.csv
│   └── payments/payments.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── spark_session.py
│   ├── schemas.py
│   ├── ingestion.py
│   ├── data_quality.py
│   ├── transformations.py
│   ├── bigquery_utils.py
│   └── main.py
├── sql/
│   └── create_tables.sql
├── dags/
│   └── customer_360_dag.py
├── tests/
│   └── test_transformations.py
├── requirements.txt
└── .gitignore
```

## Technologies

- Python
- PySpark
- Google Cloud Storage
- Google Cloud Dataproc
- BigQuery
- Apache Airflow / Cloud Composer
- Git/GitHub

## Important

Replace placeholder values such as `your-gcp-project-id`, `your-bucket` and `your-temp-bucket` with your actual GCP resources.

The current version implements the core pipeline. Incremental processing, BigQuery MERGE/upsert, audit tables and production monitoring can be added as the next phase.

## Local execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
spark-submit src/main.py
```

For Dataproc, upload the project code to GCS and submit `src/main.py` as the PySpark main file.

## Interview summary

"I built a Customer 360 pipeline using PySpark. Data from customer, order and payment systems is landed in GCS. PySpark applies explicit schemas, data-quality validation and deduplication, then performs business transformations and loads curated datasets into BigQuery. Airflow/Cloud Composer orchestrates the Dataproc job."
