import optics
import pandas as pd
import os.path

columns = [9, 10]
gps_data = pd.read_csv('/Users/mmfsf/Documents/gitcesar/projeto_portoseguro/code/clustering/data/devices/D5125505.csv', 
                            delimiter = ';', 
                            usecols = columns, 
                            names = ['latitude', 'longitude'], 
                            header = None)

gps_data = gps_data.as_matrix(columns=['latitude', 'longitude'])

points = []
for coord in gps_data:
    points.append(optics.Point(coord[0], coord[1]))

print "chegou!!"

optics = optics.Optics(points, 500, 10) # 100m radius for neighbor consideration, cluster size >= 2 points
optics.run()                    # run the algorithm
clusters = optics.cluster(50)   # 50m threshold for clustering

print len(clusters)
for cluster in clusters:
    print cluster.centroid().to_geo_json_dict