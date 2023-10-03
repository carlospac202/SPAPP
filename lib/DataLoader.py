from lib import ConfigLoader

def get_account_schema():
    schema = """load_date date, active_ind int, account_id string, id int"""
    return schema

def read_accounts(spark, env, enable_hive, hive_db):
    runtime_filter = ConfigLoader.get_data_filter(env, "account.filter")
    if enable_hive:
        return spark.sql("select * from " + hive_db + ".accounts").where(runtime_filter)
    else:
        return spark.read \
            .format("csv") \
            .option("header", "true") \
            .schema(get_account_schema()) \
            .load("test_data/files/") \
            .where(runtime_filter)
