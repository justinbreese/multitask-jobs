from utils import *

df = spark.range(100).withColumn("colE", col("id") % 2)
selCols = ["left.id", "animal", "colB", "colC", "colE"]
joinedDf = enrichedDf.alias("left").join(df.alias("right"), enrichedDf.id == df.id, "left_outer").select(*selCols)

joinedDf.write.format("delta").save(silverPath)
