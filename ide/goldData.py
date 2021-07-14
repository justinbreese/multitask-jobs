from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--savePath", help="some useful description.")
parser.add_argument("--animal", help="some useful description.")
parser.add_argument("--food", help="some useful description.")
args = parser.parse_args()

# spark = SparkSession.builder.getOrCreate()

savePath = args.savePath
animal = args.animal
food = args.food
rawPath = savePath + "/raw"
bronzePath = savePath + "/bronze"
enrichedPath = savePath + "/enriched"
silverPath = savePath + "/silver"
goldPath = savePath + "/gold"

silverDf = spark.read.format("delta").load(silverPath)

goldDf = silverDf.withColumn("food", lit(food))


# COMMAND ----------

goldDf.write.format("delta").save(goldPath)
