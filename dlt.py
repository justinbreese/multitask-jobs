# Databricks notebook source
import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

# get these values from the run
animal = spark.conf.get("my.animal")
food = spark.conf.get("my.food")

# bronze data ##############################
@dlt.table(
  comment = "this is the bronze data"
)
@dlt.expect("colB_valid_value", "colB < 49")
# @dlt.expect_or_fail("colB_valid_value", "colB < 49")
def jbreese_bronze_data():
  df = spark.range(10000).withColumn("colB", col("id") % 50).withColumn("colC", col("id") + 551)
  return df

# raw data ###############################
@dlt.table(
  comment = "this is the raw data"
)
@dlt.expect("animal_not_null", "animal is not null")
def jbreese_raw_data():
  return spark.range(1000).withColumn("animal", lit(animal))

# enriched data ############################
@dlt.table(
  comment = "this is the enriched data"
)
def jbreese_enriched_data():
  selCols = ["left.id", "animal", "colB", "colC"]
  rawDf = dlt.read("jbreese_raw_data")
  bronzeDf = dlt.read("jbreese_bronze_data")
  
  joinedDf = rawDf.alias("left").join(bronzeDf.alias("right"), rawDf.id == bronzeDf.id, "right_outer").select(*selCols)
  
  return joinedDf

# silver data ##############################
@dlt.table(
  comment = "this is the silver table"
)
@dlt.expect_or_fail("colC_not_null", "colC is not null")
def jbreese_silver_data():
  selCols = ["left.id", "animal", "colB", "colC", "colE"]
  enrichedDf = dlt.read("jbreese_enriched_data")
  df = spark.range(100).withColumn("colE", col("id") % 2)
  
  joinedDf = enrichedDf.alias("left").join(df.alias("right"), enrichedDf.id == df.id, "left_outer").select(*selCols)
  
  return joinedDf

#gold data ##############################
@dlt.table(
  comment = "this is the gold table"
)
@dlt.expect_or_fail("food_not_null", "food is not null")
def jbreese_gold_data():
  silverDf = dlt.read("jbreese_silver_data")
  goldDf = silverDf.withColumn("food", lit(food))
  return goldDf

# COMMAND ----------

###### contraint types ################
# @dlt.expect
# @dlt.expect_or_fail
# @dlt.expect_or_drop

####### parameterize/re-use expectations ##############
# idExpectation = {"id_not_null", "id is not null"}
# @dlt.expect(idExpectation)

