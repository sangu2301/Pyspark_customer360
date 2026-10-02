from pyspark.sql import SparkSession


def create_spark_session():
    return (
        SparkSession.builder
        .appName("Customer360Pipeline")
        .config("spark.sql.shuffle.partitions", "100")
        .getOrCreate()
    )
