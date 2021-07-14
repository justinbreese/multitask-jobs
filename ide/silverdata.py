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

df = spark.range(100).withColumn("colE", col("id") % 2)
selCols = ["left.id", "animal", "colB", "colC", "colE"]
joinedDf = enrichedDf.alias("left").join(df.alias("right"), enrichedDf.id == df.id, "left_outer").select(*selCols)

joinedDf.write.format("delta").save(silverPath)
