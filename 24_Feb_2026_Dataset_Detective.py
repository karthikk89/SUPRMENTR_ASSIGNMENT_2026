import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print("Highest value column:")
print(df.max())

print("Missing values:")
print(df.isnull().sum())