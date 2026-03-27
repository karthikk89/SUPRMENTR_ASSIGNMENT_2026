import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "size":[1000,1500,2000,2500],
    "price":[200000,300000,400000,500000]
}

df = pd.DataFrame(data)

X = df[["size"]]
y = df["price"]

model = LinearRegression()
model.fit(X,y)

new_size = [[1800]]

prediction = model.predict(new_size)

print("Predicted price:", prediction)