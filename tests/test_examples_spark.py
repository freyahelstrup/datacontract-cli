import logging

import pytest

from datacontract.data_contract import DataContract

from pyspark.sql import SparkSession

logging.basicConfig(level=logging.DEBUG, force=True)

datacontract = "examples/spark/datacontract.yaml"
dataset_name = "orders"

def test_examples_spark():

    # Create a SparkSession
    spark = SparkSession.builder.appName("Testing PySpark Data Contract").getOrCreate()
    
    # Read data
    path = "examples/spark/data/orders-1.json"
    df = spark.read.json(path)

    # Create view
    df.createOrReplaceTempView(dataset_name)

    # Test data contract
    data_contract = DataContract(data_contract_file=datacontract, spark=spark)
    run = data_contract.test()

    print(run)
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)
