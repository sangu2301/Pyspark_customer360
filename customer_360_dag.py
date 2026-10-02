from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocSubmitJobOperator,
)


PROJECT_ID = "your-gcp-project-id"
REGION = "asia-south1"
CLUSTER_NAME = "customer360-cluster"


with DAG(
    dag_id="customer_360_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule="@daily",
    catchup=False,
    tags=["pyspark", "bigquery", "customer360"],
) as dag:

    start = EmptyOperator(task_id="start")

    run_pyspark = DataprocSubmitJobOperator(
        task_id="run_pyspark",
        project_id=PROJECT_ID,
        region=REGION,
        job={
            "placement": {
                "cluster_name": CLUSTER_NAME,
            },
            "pyspark_job": {
                "main_python_file_uri": (
                    "gs://your-bucket/src/main.py"
                ),
            },
        },
    )

    end = EmptyOperator(task_id="end")

    start >> run_pyspark >> end
