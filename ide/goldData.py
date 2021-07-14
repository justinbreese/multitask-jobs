from utils import *

silverDf = spark.read.format("delta").load(silverPath)

goldDf = silverDf.withColumn("food", lit(food))


# COMMAND ----------

goldDf.write.format("delta").save(goldPath)
