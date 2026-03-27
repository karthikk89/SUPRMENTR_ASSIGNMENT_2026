import pandas as pd
from sklearn.cluster import KMeans

data = {
    "income":[15,16,17,80,82,85],
    "spending":[39,40,41,90,92,95]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=2)
df["cluster"] = kmeans.fit_predict(df)

print(df)