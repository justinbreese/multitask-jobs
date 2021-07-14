// Databricks notebook source
// MAGIC %run ./utils

// COMMAND ----------

val rawDf = spark.read.format("delta").load(rawPath)
val bronzeDf = spark.read.format("delta").load(bronzePath)

// COMMAND ----------

val joinedDf = rawDf.join(bronzeDf, Seq("id"), "right_outer")

// COMMAND ----------

display(joinedDf)

// COMMAND ----------

joinedDf.write.format("delta").save(enrichedPath)
