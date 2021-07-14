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

# COMMAND ----------

rawDf = spark.read.format("delta").load(rawPath)
bronzeDf = spark.read.format("delta").load(bronzePath)

# COMMAND ----------

joinedDf = rawDf.join(bronzeDf, rawDf.id == bronzeDf.id, "right_outer")

# COMMAND ----------

joinedDf.write.format("delta").save(enrichedPath)
