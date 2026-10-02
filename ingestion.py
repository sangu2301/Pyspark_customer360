from schemas import customer_schema, order_schema, payment_schema


def read_customers(spark, path):
    return (
        spark.read
        .schema(customer_schema)
        .option("header", True)
        .csv(path)
    )


def read_orders(spark, path):
    return (
        spark.read
        .schema(order_schema)
        .option("header", True)
        .csv(path)
    )


def read_payments(spark, path):
    return (
        spark.read
        .schema(payment_schema)
        .option("header", True)
        .csv(path)
    )
