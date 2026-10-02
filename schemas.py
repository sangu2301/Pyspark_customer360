from pyspark.sql.types import (
    StructType,
    StructField,
    LongType,
    StringType,
    DoubleType,
    IntegerType,
    TimestampType,
)


customer_schema = StructType([
    StructField("customer_id", LongType(), False),
    StructField("customer_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("country", StringType(), True),
    StructField("customer_type", StringType(), True),
    StructField("updated_timestamp", TimestampType(), True),
])


order_schema = StructType([
    StructField("order_id", LongType(), False),
    StructField("customer_id", LongType(), False),
    StructField("product_id", LongType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("amount", DoubleType(), True),
    StructField("status", StringType(), True),
    StructField("updated_timestamp", TimestampType(), True),
])


payment_schema = StructType([
    StructField("payment_id", LongType(), False),
    StructField("customer_id", LongType(), False),
    StructField("order_id", LongType(), False),
    StructField("amount", DoubleType(), True),
    StructField("payment_status", StringType(), True),
    StructField("payment_method", StringType(), True),
    StructField("updated_timestamp", TimestampType(), True),
])
