// Databricks notebook source
// MAGIC %run ./utils

// COMMAND ----------

val enrichedDf = spark.read.format("delta").load(enrichedPath)
val df = spark.range(100).withColumn("colE", 'id % 2)
val selCols = List("left.id", "animal", "colB", "colC", "colE")

// COMMAND ----------

val joinedDf = enrichedDf.alias("left").join(df.alias("right"), $"left.colB" === $"right.colE", "left_outer").select(selCols.map(col): _*)

// COMMAND ----------

display(joinedDf)

// COMMAND ----------

joinedDf.write.format("delta").save(silverPath)
