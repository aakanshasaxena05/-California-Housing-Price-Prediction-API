from sklearn.datasets import fetch_california_housing
import pandas as pd
data=fetch_california_housing()
df=pd.DataFrame(data.data,columns=data.feature_names)
df["Price"]=data.target
print("shape",df.shape)
print(df.head())
print(df.describe())
print(data.feature_names)