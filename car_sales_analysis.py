import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('C:\\Users\\HOME\\Downloads\\car_dataset\\CarPrice_Assignment.csv')
print('Data Loaded Successfully')

print('\nPreview of Dataset:\n',df.head())
print("Dataset Info\n")
print(df.info())
print('\nMissing Values\n',df.isnull().sum())
print('Summary Statistics\n',df.describe())
df['Brand'] = df['CarName'].apply(lambda x: x.split()[0].lower())
print('\nNo of cars by brand\n',df['Brand'].value_counts())
avg_price=df.groupby('Brand')['price'].mean()
print("\nAverage price of the cars by brand\n",avg_price)

plt.figure(figsize=(8,5))
sns.countplot(x='Brand',data=df,palette='Set2',order=df['Brand'].value_counts().index)
plt.title('Number of Cars by Brands')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6))
df['fueltype'].value_counts().plot.pie(autopct='%1.1f%%',startangle=90,colors=sns.color_palette('pastel'))
plt.title('Fuel Type Distribution')
plt.ylabel('')
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='carbody',y='price',data=df,palette='coolwarm')
plt.title('Price by CarBody')
plt.show()
