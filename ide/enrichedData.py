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
selCols = ["left.id", "animal", "colB", "colC"]

# COMMAND ----------

rawDf = spark.read.format("delta").load(rawPath)
bronzeDf = spark.read.format("delta").load(bronzePath)

# COMMAND ----------

joinedDf = rawDf.alias("left").join(bronzeDf.alias("right"), rawDf.id == bronzeDf.id, "right_outer").select(*selCols)

# COMMAND ----------

joinedDf.write.format("delta").save(enrichedPath)
