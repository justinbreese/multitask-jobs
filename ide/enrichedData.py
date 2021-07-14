from utils import *

# COMMAND ----------

rawDf = spark.read.format("delta").load(rawPath)
bronzeDf = spark.read.format("delta").load(bronzePath)

# COMMAND ----------

joinedDf = rawDf.join(bronzeDf, rawDf.id == bronzeDf.id, "right_outer")

# COMMAND ----------

joinedDf.write.format("delta").save(enrichedPath)
