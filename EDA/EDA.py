# Databricks notebook source
import pandas as pd

pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 25)

# COMMAND ----------



# COMMAND ----------

df = pd.read_csv("/dbfs/mnt/data/flickr/yfcc100m_dataset-0.bz2", sep="\t")

# COMMAND ----------

df.info()

# COMMAND ----------

df.columns = ["Photo/video identifier","User NSID","User nickname","Date taken","Date uploaded","Capture device","Title",
           "Description","User tags (comma-separated)","Machine tags (comma-separated)","Longitude","Latitude","Accuracy",
           "Photo/video page URL","Photo/video download URL","License name","License URL","Photo/video server identifier",
           "Photo/video farm identifier","Photo/video secret","Photo/video secret original","Photo/video extension original",
           "Photos/video marker (0 = photo, 1 = video)"]

df.head(10)

# COMMAND ----------

df = df.drop(["Photo/video identifier","User NSID","User nickname","Date uploaded","Capture device","Machine tags (comma-separated)",
        "Photo/video page URL","License name","License URL","Photo/video server identifier","Photo/video farm identifier","Photo/video secret",
         "Photo/video secret original","Photo/video extension original"], axis=1)

# COMMAND ----------

df = df[~df["Photos/video marker (0 = photo, 1 = video)"].astype(str).str.contains('1')]

# COMMAND ----------

len(df.index)

# COMMAND ----------

df = df.drop(["Photos/video marker (0 = photo, 1 = video)"], axis=1)

# COMMAND ----------

df.head(0)

# COMMAND ----------

df1=df
df1 = df1.drop(["User tags (comma-separated)","Title","Description"], axis=1)

# COMMAND ----------

df1.head()

# COMMAND ----------

len(df1.index)

# COMMAND ----------

df1.dropna( axis=0, how='any', thresh=None, subset=["Photo/video download URL"], inplace=False)

# COMMAND ----------

subsetDataFrame = df1[df1['Longitude'].isnull()]

print((len(subsetDataFrame.index)/len(df1.index))*100)

# COMMAND ----------

df2=df1
df2=df2.dropna(subset=["Longitude","Latitude"])
len(df2.index)

# COMMAND ----------

df2.head()
dfLatLong =df2.drop(["Date taken","Accuracy","Photo/video download URL"], axis=1)


# COMMAND ----------

dt.head()

# COMMAND ----------



# COMMAND ----------

#dt=dfLatLong[['Latitude','Longitude']].iloc[ 10000:12000 , : ]
dt=dfLatLong[['Latitude','Longitude']]
fi=dt.to_string(index=False).replace("  ", ",")
fi.to_csv("/dbfs/mnt/group17/latlong.csv", index=False)
#print(dt.to_string(index=False).replace("  ", ","))
print(fi)

# COMMAND ----------

df2["Accuracy"].describe()

# COMMAND ----------

	
df1.duplicated(subset="Photo/video download URL", keep='first')

# COMMAND ----------

df['Accuracy'].value_counts()