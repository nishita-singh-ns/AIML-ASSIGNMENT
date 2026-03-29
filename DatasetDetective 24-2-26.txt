### CODE CELL ###
import pandas as pd

data = pd.read_excel("data.xlsx")

print("Top 5 Rows:")
display(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

numeric_data = data.select_dtypes(include='number')
max_values = numeric_data.max()

print("\nColumn with Highest Value:")
print(max_values.idxmax())

