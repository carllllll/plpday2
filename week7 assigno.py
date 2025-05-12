import pandas as pd

# Load the dataset from seaborn (comes with Iris)
import seaborn as sns
df = sns.load_dataset('iris')

# Display first few rows
print(df.head())

print(df.dtypes)

print(df.isnull().sum())

df=df.dropna()

print(df.describe())
grouped= df.groupby('species').mean()
print(grouped)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
df_sorted=df.groupby('species')['petal_length'].mean().reset_index()

#Line chart
plt.figure(figsize=(6, 4))
sns.lineplot(data=df_sorted, x='species', y='petal_length', marker='o')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

#Bar chart
plt.figure(figsize=(6, 4))
sns.barplot(data=df_sorted, x='species', y='sepal_width')
plt.title('Average Sepal Width by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width')
plt.show()

#Histogram
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='petal_length', bins=20, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.show()


