import pandas as pd
import matplotlib.pylab as plt
filename=("C:\\Users\\hp\\Desktop\\AI_Lab\\Activity03\\auto.csv")
headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpa","city=mpg","highway-mpg","price"]
df=pd.read_csv(filename,names=headers)
df.head()
import numpy as np
df.replace("?",np.nan,inplace=True)
df.head(5)
missing_data = df.isnull()
missing_data.head(5)
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:",avg_norm_loss)
# Replace "NaN" with mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan,avg_norm_loss,inplace=True)
df.head()
# Calculate the mean value for "bore" column
avg_bore=df['bore'].astype('float').mean(axis=0)
print('Average of bore:',avg_bore)
# Replace "NaN" with mean value in the "bore" column
df["bore"].replace(np.nan,avg_bore,inplace=True)
df.head()
# replace NaN in "stroke" column with mean value
avg_stroke = df["stroke"].astype("float").mean(axis=0)
print("Average of stroke:",avg_stroke)
df["stroke"].replace(np.nan,avg_norm_loss,inplace=True)
df.head()
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
# Calculate he mean value for "peak-rpm" column
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)