# 📊 Real-world Data Analysis Project (Retail)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

# -------------------------------
# Data Understanding
# -------------------------------
print("\nInfo:")
df.info()

print("\nSummary:")
print(df.describe())

# -------------------------------
# Data Cleaning
# -------------------------------
df.dropna(inplace=True)

# -------------------------------
# Analysis & Visualization
# -------------------------------

# Total Sales by Category
plt.figure(figsize=(6,4))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.show()

# Profit by Region
plt.figure(figsize=(6,4))
df.groupby("Region")["Profit"].sum().plot(kind="bar", color='green')
plt.title("Profit by Region")
plt.show()

# Sales Trend
plt.figure(figsize=(8,4))
df.groupby("Order Date")["Sales"].sum().head(50).plot()
plt.title("Sales Trend")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Insights
# -------------------------------
print("\nKey Insights:")
print("1. Technology category usually has highest sales.")
print("2. Some regions generate more profit than others.")
print("3. Sales fluctuate over time.")
print("4. Discounts may affect profit.")

# -------------------------------
# Conclusion
# -------------------------------
print("\nConclusion:")
print("Retail data analysis helps businesses understand performance and improve decisions.")
