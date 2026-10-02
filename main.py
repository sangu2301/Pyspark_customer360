from spark_session import create_spark_session

from ingestion import (
    read_customers,
    read_orders,
    read_payments,
)

from data_quality import (
    validate_customers,
    validate_orders,
    validate_payments,
)

from transformations import (
    deduplicate,
    create_customer_360,
)

from bigquery_utils import write_to_bigquery

from config import (
    PROJECT_ID,
    RAW_PATH,
    REJECTED_PATH,
    TEMP_BUCKET_NAME,
    BIGQUERY_DATASET,
    CUSTOMER_TABLE,
    ORDER_TABLE,
    PAYMENT_TABLE,
    CUSTOMER_360_TABLE,
)


def main():
    spark = create_spark_session()

    try:
        print("=== CUSTOMER 360 PIPELINE STARTED ===")

        customers = read_customers(
            spark, f"{RAW_PATH}/customers"
        )
        orders = read_orders(
            spark, f"{RAW_PATH}/orders"
        )
        payments = read_payments(
            spark, f"{RAW_PATH}/payments"
        )

        print("Raw data loaded")

        customers, rejected_customers = validate_customers(
            customers
        )
        orders, rejected_orders = validate_orders(
            orders
        )
        payments, rejected_payments = validate_payments(
            payments
        )

        rejected_customers.write.mode("append").parquet(
            f"{REJECTED_PATH}/customers"
        )
        rejected_orders.write.mode("append").parquet(
            f"{REJECTED_PATH}/orders"
        )
        rejected_payments.write.mode("append").parquet(
            f"{REJECTED_PATH}/payments"
        )

        customers = deduplicate(customers, "customer_id")
        orders = deduplicate(orders, "order_id")
        payments = deduplicate(payments, "payment_id")

        print("Validation and deduplication completed")

        write_to_bigquery(
            customers,
            PROJECT_ID,
            BIGQUERY_DATASET,
            CUSTOMER_TABLE,
            TEMP_BUCKET_NAME,
        )

        write_to_bigquery(
            orders,
            PROJECT_ID,
            BIGQUERY_DATASET,
            ORDER_TABLE,
            TEMP_BUCKET_NAME,
        )

        write_to_bigquery(
            payments,
            PROJECT_ID,
            BIGQUERY_DATASET,
            PAYMENT_TABLE,
            TEMP_BUCKET_NAME,
        )

        customer_360 = create_customer_360(
            customers,
            orders,
            payments,
        )

        write_to_bigquery(
            customer_360,
            PROJECT_ID,
            BIGQUERY_DATASET,
            CUSTOMER_360_TABLE,
            TEMP_BUCKET_NAME,
        )

        print("=== CUSTOMER 360 PIPELINE COMPLETED ===")

    finally:
        spark.stop()


if __name__ == "__main__":
    main()
