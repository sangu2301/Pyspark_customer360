from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number, count, sum, max


def deduplicate(df, key):
    window_spec = (
        Window
        .partitionBy(key)
        .orderBy(col("updated_timestamp").desc())
    )

    return (
        df.withColumn("row_num", row_number().over(window_spec))
        .filter(col("row_num") == 1)
        .drop("row_num")
    )


def create_customer_360(customers, orders, payments):
    completed_orders = orders.filter(
        col("status") == "COMPLETED"
    )

    successful_payments = payments.filter(
        col("payment_status") == "SUCCESS"
    )

    order_summary = (
        completed_orders
        .groupBy("customer_id")
        .agg(
            count("order_id").alias("total_orders"),
            sum("amount").alias("total_order_amount"),
            max("updated_timestamp").alias("last_order_timestamp"),
        )
    )

    payment_summary = (
        successful_payments
        .groupBy("customer_id")
        .agg(
            sum("amount").alias("total_paid_amount"),
            max("updated_timestamp").alias("last_payment_timestamp"),
        )
    )

    customer_360 = (
        customers
        .join(order_summary, "customer_id", "left")
        .join(payment_summary, "customer_id", "left")
        .fillna({
            "total_orders": 0,
            "total_order_amount": 0,
            "total_paid_amount": 0,
        })
    )

    return customer_360
