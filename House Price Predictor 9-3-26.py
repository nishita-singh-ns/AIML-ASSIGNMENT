### CODE CELL ###
from sklearn.linear_model import LinearRegression
import numpy as np

# Example dataset
house_size = np.array([[500],[700],[900],[1100],[1300]])
price = np.array([100000,150000,200000,250000,300000])

# Train model
model = LinearRegression()
model.fit(house_size, price)

# Predict new house price
new_size = [[1010]]
predicted_price = model.predict(new_size)

print("Predicted Price:", predicted_price)

### CODE CELL ###


