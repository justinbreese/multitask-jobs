from utils import *

df = spark.range(10000).withColumn("colB", col("id") % 50).withColumn("colC", col("id") + 551)


# COMMAND ----------

df.write.format("delta").save(bronzePath)
