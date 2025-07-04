import numpy as np
from pathmap import pathmap

# initialize hazard and crowd maps
hazards = np.zeros((30, 30))
crowd = np.zeros((30, 30))

# simulate fire zone
hazards[10:12, 10:15] = 5

# simulate dense crowd
crowd[15:20, 15:20] = 3

# define start position
start = (5, 5)

# run the algorithm
dist, prev = pathmap(start)

# visualize or print results
print("Minimum distance map from start:")
print(dist)
