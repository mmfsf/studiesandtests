import pandas
from sklearn.neighbors import BallTree
import sklearn.cluster
import numpy as np

gps_positions = pandas.read_csv('/Users/mmfsf/Documents/gitcesar/projeto_portoseguro/code/clustering/data/devices/M08403962.csv', 
                            delimiter = ';', 
                            usecols = [9, 10], 
                            names = ['latitude', 'longitude'], 
                            header = None)

# gps_data = gps_positions.as_matrix(columns=['latitude', 'longitude'])
# earth_radius = 6371.0088
# epsilon = 0.2 / earth_radius
# db = sklearn.cluster.DBSCAN(eps = epsilon, 
#                             min_samples = 5,
#                             algorithm = 'ball_tree', 
#                             metric = 'haversine').fit(np.radians(gps_data))
# cluster_labels = db.labels_
# # Number of clusters in cluster_labels, ignoring noise if present.
# num_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
# clusters = pandas.Series([gps_data[cluster_labels == n] for n in range(num_clusters)])

# print clusters

# np.savetxt("foo.csv", gps_positions, delimiter=",")

X = gps_positions
tree = BallTree(X, leaf_size=20, metric='haversine')              
dist, ind = tree.query([-23.9183, -46.5558], k = 3)                
print ind  # indices of 3 closest neighbors
print dist  # distances to 3 closest neighbors