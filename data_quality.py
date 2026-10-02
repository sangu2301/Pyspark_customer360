from pyspark.sql.functions import col


def validate_orders(orders):
    invalid_condition = (
        col("order_id").isNull()
        | col("customer_id").isNull()
        | col("amount").isNull()
        | (col("amount") < 0)
    )

    return (
        orders.filter(~invalid_condition),
        orders.filter(invalid_condition),
    )


def validate_customers(customers):
    invalid_condition = (
        col("customer_id").isNull()
        | col("email").isNull()
    )

    return (
        customers.filter(~invalid_condition),
        customers.filter(invalid_condition),
    )


def validate_payments(payments):
    invalid_condition = (
        col("payment_id").isNull()
        | col("customer_id").isNull()
        | col("amount").isNull()
        | (col("amount") < 0)
    )

    return (
        payments.filter(~invalid_condition),
        payments.filter(invalid_condition),
    )
