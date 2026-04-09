import pandas as pd

# Creating dataset
data = pd.DataFrame({
    "Study_Hours": [1,2,3,4,5,6],
    "Marks": [30,45,55,65,80,90]
})

print(data)

# Identify Features and Labels
X = data["Study_Hours"]  # Feature
y = data["Marks"]        # Label

print("\nFeature (Study Hours):")
print(X)

print("\nLabel (Marks):")
print(y)