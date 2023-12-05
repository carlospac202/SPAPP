import os

from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
from pyspark.sql import functions as F


def extract_filename(full_path):
    return os.path.basename(full_path)


extract_filename_udf = udf(extract_filename, StringType())


def transform_df(df):
    df = df.withColumn("filename", F.regexp_replace(extract_filename_udf(F.input_file_name()), "\.csv$", ""))
    df = df.groupBy("unique_id").pivot("filename").agg(F.lit(1).alias("value")).fillna(0)
    return df
