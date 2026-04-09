### CODE CELL ###
from sklearn.neighbors import NearestNeighbors
import numpy as np

data = np.array([
    [5,4,0],  # User1
    [4,0,5],  # User2
    [0,4,5],  # User3
    [0,5,4]   # User4
])

model = NearestNeighbors(n_neighbors=2)
model.fit(data)

distances, indices = model.kneighbors([data[0]])

print("Most similar users:", indices)

### CODE CELL ###


