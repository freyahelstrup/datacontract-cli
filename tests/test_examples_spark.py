import logging

from datacontract.data_contract import DataContract

from pyspark.sql import SparkSession
from pyspark.sql.types import *

logging.basicConfig(level=logging.DEBUG, force=True)

datacontract = "examples/spark/datacontract.yaml"
dataset_name = "orders"

def test_examples_spark():

    # Create a SparkSession
    spark = SparkSession.builder.appName("Testing PySpark Data Contract").getOrCreate()
    
    # Read data
    df = _prepare_df(spark)

    # Create view
    df.createOrReplaceTempView(dataset_name)

    # Test data contract
    data_contract = DataContract(data_contract_file=datacontract, spark=spark)
    run = data_contract.test()

    print(run)
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)

def _prepare_df(spark):
    path = "examples/spark/data/orders-1.json"
    schema = StructType([
      StructField("order_id", StringType(), True),
      StructField("order_timestamp", TimestampType(), True),
      StructField("order_total", LongType(), True),
      StructField("customer_id", StringType(), True),
      StructField("customer_email_address", StringType(), True)]
    )
    df = spark.read.schema(schema).json(path)
    return df
