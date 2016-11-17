from sklearn.neighbors import NearestNeighbors
import pandas
from sklearn.neighbors import BallTree
import sklearn.cluster
import numpy as np

gps_positions = pandas.read_csv('/Users/mmfsf/Documents/gitcesar/projeto_portoseguro/code/clustering/data/devices/M08403962.csv', 
                            delimiter = ';', 
                            usecols = [9, 10], 
                            names = ['latitude', 'longitude'], 
                            header = None)

nbrs = NearestNeighbors(n_neighbors=20, algorithm='ball_tree', metric = 'haversine').fit(gps_positions)
distances, indices = nbrs.kneighbors([-23.478936, -46.600562])
print indices
print distances