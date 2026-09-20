from pyspark.sql import SparkSession
s=SparkSession.builder.appName("batch").getOrCreate();d=s.read.parquet("s3a://analytics-raw/events/").dropDuplicates(["event_id"]).filter("event_id is not null");d.write.mode("overwrite").partitionBy("event_type").parquet("s3a://analytics-curated/batch/")
