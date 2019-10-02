# Databricks notebook source
import pandas as pd

# pd.set_option('display.max_colwidth', 200)
# pd.set_option('display.max_columns', 25)

bCounter = 0
aCounter = 0
a = 0
b = 0
naCounter = 0
vidCounter = 0

for i in range (0, 10):
  in_path = "/dbfs/mnt/data/flickr/yfcc100m_dataset-" + str(i) + ".bz2"
  df = pd.read_csv(in_path, sep="\t")

  df.columns = ["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Title",
           "Description","User tags (comma-separated)","Machine tags (comma-separated)","Longitude","Latitude","Accuracy",
           "Photo/video page URL","Photo/video download URL","License name","License URL","Photo/video server identifier",
           "Photo/video farm identifier","Photo/video secret","Photo/video secret original","Photo/video extension original",
           "Photos/video marker (0 = photo, 1 = video)"]

  bCounter = bCounter + len(df.index)
  a = len(df.index)
  
  df = df.drop(["Photo/video identifier","User NSID","User nickname","Date uploaded","Capture device","Machine tags (comma-separated)",
        "Photo/video page URL","License name","License URL","Photo/video server identifier","Photo/video farm identifier","Photo/video secret",
         "Photo/video secret original","Photo/video extension original"], axis=1)
  
  df = df[~df["Photos/video marker (0 = photo, 1 = video)"].astype(str).str.contains('1')]
  b = len(df.index)
  
  vidCounter = vidCounter + (a - b)
  
  df = df.drop(["Photos/video marker (0 = photo, 1 = video)"], axis=1)
  a = len(df.index)
  
  df = df.dropna(subset=["Longitude","Latitude"])
  b = len(df.index)
  
  naCounter = naCounter + (a - b)
  
  aCounter = aCounter + len(df.index)
  
  out_path = "/dbfs/mnt/group17/clean-" + str(i) + ".csv"
  df.to_csv(out_path, index=False)

print("Before: " + str(bCounter))
print("After: " + str(aCounter))
print("NaN's in Lat & Long: " + str(naCounter))
print("Videos: " + str(vidCounter))

# COMMAND ----------

import pandas as pd

df = pd.read_csv("/dbfs/mnt/group17/clean-0.csv")
df.columns = ["Date taken","Title","Description","User tags (comma-separated)","Longitude","Latitude","Accuracy","Photo/video download URL"]

for i in range (1, 10):
  in_path = "/dbfs/mnt/group17/clean-" + str(i) + ".csv"
  df1 = pd.read_csv(in_path)
  df = df.append(df1, ignore_index=True)
  
print(len(df.index))
print(df['Accuracy'].value_counts())

# COMMAND ----------

# df = pd.read_csv("/dbfs/mnt/data/flickr/yfcc100m_dataset-0.bz2", sep="\t")

# COMMAND ----------

# DBTITLE 1,Assign names to columns
# df.columns = ["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Title",
#            "Description","User tags (comma-separated)","Machine tags (comma-separated)","Longitude","Latitude","Accuracy",
#            "Photo/video page URL","Photo/video download URL","License name","License URL","Photo/video server identifier",
#            "Photo/video farm identifier","Photo/video secret","Photo/video secret original","Photo/video extension original",
#            "Photos/video marker (0 = photo, 1 = video)"]

# len(df.index)

# COMMAND ----------

# DBTITLE 1,Drop unwanted columns
# df = df.drop(["Photo/video identifier","User NSID","User nickname","Date uploaded","Capture device","Machine tags (comma-separated)",
#         "Photo/video page URL","License name","License URL","Photo/video server identifier","Photo/video farm identifier","Photo/video secret",
#          "Photo/video secret original","Photo/video extension original"], axis=1)

# COMMAND ----------

# DBTITLE 1,Drop videos
# df = df[~df["Photos/video marker (0 = photo, 1 = video)"].astype(str).str.contains('1')]
# len(df.index)

# COMMAND ----------

# DBTITLE 1,Drop column Photos/video marker
# df = df.drop(["Photos/video marker (0 = photo, 1 = video)"], axis=1)

# COMMAND ----------

# DBTITLE 1,Drop rows having NaN as Latitude and Longitude
# df = df.dropna(subset=["Longitude","Latitude"])
# len(df.index)

# COMMAND ----------

# df.head(10)

# COMMAND ----------

# DBTITLE 1,Save dataframe as csv
# df.to_csv("/dbfs/mnt/group17/clean-0.csv", index=False)