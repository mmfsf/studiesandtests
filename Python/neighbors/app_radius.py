import numpy as np
import sklearn.neighbors as sn

np.random.seed(0)
X = np.random.random((10, 3))  # 10 points in 3 dimensions
tree = sn.BinaryTree(X, leaf_size=2)     
print tree.query_radius(X[0], r=0.3, count_only=True)

ind = tree.query_radius(X[0], r=0.3)  
print ind  # indices of neighbors within distance 0.3