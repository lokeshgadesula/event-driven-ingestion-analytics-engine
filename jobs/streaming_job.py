from pyspark.sql import SparkSession
from pyspark.sql.functions import col,from_json,window,count,sum as ssum
from pyspark.sql.types import *
spark=SparkSession.builder.appName("events").getOrCreate()
schema=StructType([StructField("event_id",StringType()),StructField("event_type",StringType()),StructField("timestamp",StringType()),StructField("value",DoubleType())])
raw=spark.readStream.format("kafka").option("kafka.bootstrap.servers","kafka:9092").option("subscribe","events").load()
e=raw.select(from_json(col("value").cast("string"),schema).alias("x")).select("x.*").withColumn("event_time",col("timestamp").cast("timestamp")).withWatermark("event_time","10 minutes").dropDuplicates(["event_id"])
a=e.groupBy(window("event_time","5 minutes"),"event_type").agg(count("*").alias("event_count"),ssum("value").alias("value_sum"))
a.writeStream.outputMode("update").format("parquet").option("path","s3a://analytics-curated/stream").option("checkpointLocation","s3a://analytics-curated/checkpoints").start().awaitTermination()
