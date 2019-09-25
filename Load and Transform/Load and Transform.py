# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.read_csv("/mnt/group17/flickr/yfcc100m_dataset-0.bz2", sep="\t")
df.columns = ["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Title",
           "Description","User tags (comma-separated)","Machine tags (comma-separated)","Longitude","Latitude","Accuracy",
           "Photo/video page URL","Photo/video download URL","License name","License URL","Photo/video server identifier",
           "Photo/video farm identifier","Photo/video secret","Photo/video secret original","Photo/video extension original",
           "Photos/video marker (0 = photo, 1 = video)"]

# COMMAND ----------

pd.set_option('display.max_colwidth', 400)
df.head(10)