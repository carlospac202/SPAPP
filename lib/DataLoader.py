def get_table_schema():
    schema = """unique_id string"""
    return schema


def read_input_file(spark):
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_table_schema()) \
        .load("test_data/*")
