import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('sales_data.csv')

# Data Cleaning
data['Date'] = pd.to_datetime(data['Date'])
print(data.info())

# Handling missing values (if any)
data = data.dropna()

# Summary Statistics
print(data.describe())

# EDA
# Distribution of Sales Amount
plt.figure(figsize=(10, 6))
sns.histplot(data['Sales_Amount'], kde=True)
plt.title('Distribution of Sales Amount')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# Time Series Plot
plt.figure(figsize=(10, 6))
data.set_index('Date')['Sales_Amount'].plot()
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.show()

# Sales Performance by Region
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Sales_Amount', data=data)
plt.title('Sales Performance by Region')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
plt.show()

# Best-Selling Product
best_selling_product = data.groupby('Product').sum()[['Sales_Amount', 'Sales_Units']]
print(best_selling_product)
