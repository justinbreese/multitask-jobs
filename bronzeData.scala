// Databricks notebook source
// MAGIC %run ./utils

// COMMAND ----------

import org.apache.spark.sql.functions._

val df = spark.range(10000).withColumn("colB", 'id % 50).withColumn("colC", 'id + 551)

// COMMAND ----------

display(df)

// COMMAND ----------

df.write.format("delta").save(bronzePath)
