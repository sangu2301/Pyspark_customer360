def write_to_bigquery(
    dataframe,
    project_id,
    dataset,
    table,
    temporary_gcs_bucket,
    mode="overwrite",
):
    table_id = f"{project_id}.{dataset}.{table}"

    (
        dataframe.write
        .format("bigquery")
        .option("table", table_id)
        .option("temporaryGcsBucket", temporary_gcs_bucket)
        .mode(mode)
        .save()
    )
