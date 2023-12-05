import sys

from lib import DataLoader, Utils, Transformations
from lib.logger import Log4j

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: spapp {local, qa, prod} {load_date} : Arguments are missing")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = Utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    logger.info("Reading files...")

    df = DataLoader.read_input_file(spark)
    df = Transformations.transform_df(df)

    logger.info(df.show())