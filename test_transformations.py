from pyspark.sql import SparkSession

from src.transformations import deduplicate


def test_deduplicate():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test")
        .getOrCreate()
    )

    data = [
        (1001, 500.0, "2026-10-01 10:00:00"),
        (1001, 800.0, "2026-10-01 11:00:00"),
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "amount", "updated_timestamp"],
    )

    # Convert string timestamp for the test.
    from pyspark.sql.functions import to_timestamp
    df = df.withColumn(
        "updated_timestamp",
        to_timestamp("updated_timestamp")
    )

    result = deduplicate(df, "order_id")

    assert result.count() == 1
    assert result.first()["amount"] == 800.0

    spark.stop()
