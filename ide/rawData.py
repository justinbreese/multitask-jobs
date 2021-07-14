from utils import *

df = spark.range(1000).withColumn("animal", lit(animal))

df.write.format("delta").save(rawPath)
