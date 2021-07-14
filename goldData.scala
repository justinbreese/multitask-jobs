// Databricks notebook source
// MAGIC %run ./utils

// COMMAND ----------

val silverDf = spark.read.format("delta").load(silverPath)
display(silverDf)

// COMMAND ----------

val goldDf = silverDf.withColumn("food", lit(food))
display(goldDf)

// COMMAND ----------

goldDf.write.format("delta").save(goldPath)
