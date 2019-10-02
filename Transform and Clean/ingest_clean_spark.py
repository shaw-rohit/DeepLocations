# Databricks notebook source
"""
refine types?
["DataType", "NullType", "StringType", "BinaryType", "BooleanType", "DateType",
    "TimestampType", "DecimalType", "DoubleType", "FloatType", "ByteType", "IntegerType",
    "LongType", "ShortType", "ArrayType", "MapType", "StructField", "StructType"]
"""

# COMMAND ----------

from pyspark.sql.types import *

schema = StructType()\
  .add("Photo/video identifier", LongType(), True)\
  .add("User NSID", StringType(), True)\
  .add("User nickname", StringType(), True)\
  .add("Date taken", StringType(), True)\
  .add("Date uploaded", IntegerType(), True)\
  .add("Capture device", StringType(), True)\
  .add("Title", StringType(), True)\
  .add("Description", StringType(), True)\
  .add("User tags (comma-separated)", StringType(), True)\
  .add("Machine tags (comma-separated)", StringType(), True)\
  .add("Longitude", DoubleType(), True)\
  .add("Latitude", DoubleType(), True)\
  .add("Accuracy", IntegerType(), True)\
  .add("Photo/video page URL", StringType(), True)\
  .add("Photo/video download URL", StringType(), True)\
  .add("License name", StringType(), True)\
  .add("License URL", StringType(), True)\
  .add("Photo/video server identifier", IntegerType(), True)\
  .add("Photo/video farm identifier", IntegerType(), True)\
  .add("Photo/video secret", StringType(), True)\
  .add("Photo/video secret original", StringType(), True)\
  .add("Photo/video extension original", StringType(), True)\
  .add("Photos/video marker (0 = photo, 1 = video)", IntegerType(), True)\

# COMMAND ----------

bCounter = 0
aCounter = 0

for i in range (0, 10):
  in_path = "/mnt/data/flickr/yfcc100m_dataset-" + str(i) + ".bz2"
  df = spark.read.format("csv").option("delimiter","\t").schema(schema).load(in_path)
  
  bCounter = bCounter + df.count()
  
  df = df.select("Date taken",
               "Title", 
               "Description",
               "User tags (comma-separated)",
               "Longitude",
               "Latitude",
               "Accuracy",
               "Photo/video download URL",
               "Photos/video marker (0 = photo, 1 = video)")\
       .where((df["Photos/video marker (0 = photo, 1 = video)"] == 0) &
              (df["Longitude"].isNotNull()) &
              (df["Latitude"].isNotNull()))\
       .drop("Photos/video marker (0 = photo, 1 = video)")
  
  aCounter = aCounter + df.count()
  
  out_path = "/mnt/group17/spark_clean-" + str(i) + ".csv"
  df.write.csv(out_path)

# COMMAND ----------

print("Before: " + str(bCounter))
print("After: " + str(aCounter))

p = (aCounter/bCounter)*100
print("Percentage usable: " + str(p) + "%")