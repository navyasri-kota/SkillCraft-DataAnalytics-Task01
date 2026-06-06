import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("task1.csv")
print(df.head())
# Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
# Bar Chart
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6,4))
gender_counts.plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()