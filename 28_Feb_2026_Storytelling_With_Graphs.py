import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["A","B","C","D"],
    "Sales": [100,150,80,200]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales")
plt.show()

# Pie Chart
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.show()

# Histogram
plt.hist(df["Sales"])
plt.show()