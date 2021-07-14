// Databricks notebook source
// MAGIC %run ./utils

// COMMAND ----------

import org.apache.spark.sql.functions._

val df = spark.range(1000).withColumn("animal", lit(animal))

// COMMAND ----------

display(df)

// COMMAND ----------

df.write.format("delta").save(rawPath)
