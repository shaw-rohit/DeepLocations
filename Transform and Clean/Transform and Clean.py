# Databricks notebook source
import pandas as pd

pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 25)

# COMMAND ----------

df = pd.read_csv("/dbfs/mnt/data/flickr/yfcc100m_dataset-0.bz2", sep="\t")

# COMMAND ----------

# Assign names to columns
df.columns = ["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Title",
           "Description","User tags (comma-separated)","Machine tags (comma-separated)","Longitude","Latitude","Accuracy",
           "Photo/video page URL","Photo/video download URL","License name","License URL","Photo/video server identifier",
           "Photo/video farm identifier","Photo/video secret","Photo/video secret original","Photo/video extension original",
           "Photos/video marker (0 = photo, 1 = video)"]

len(df.index)

# COMMAND ----------

# Drop unwanted columns
df = df.drop(["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Machine tags (comma-separated)",
        "Photo/video page URL","License name","License URL","Photo/video server identifier","Photo/video farm identifier","Photo/video secret",
         "Photo/video secret original","Photo/video extension original"], axis=1)

# COMMAND ----------

# Drop videos
df = df[~df["Photos/video marker (0 = photo, 1 = video)"].astype(str).str.contains('1')]
len(df.index)

# COMMAND ----------

# Drop column Photos/video marker
df = df.drop(["Photos/video marker (0 = photo, 1 = video)"], axis=1)

# COMMAND ----------

# Drop rows having NaN as Latitude and Longitude
df = df.dropna(subset=["Longitude","Latitude"])
len(df.index)

# COMMAND ----------

df.head(10)

# COMMAND ----------

# Save dataframe as csv
df.to_csv("/dbfs/mnt/group17/clean-0.csv", index=False)