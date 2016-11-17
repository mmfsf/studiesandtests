import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from sklearn.preprocessing import StandardScaler

## Calculate the centermost point in the cluster
#
#  The cluster will have a set of points. The centroid of these points is calculated and the point closer to the
#  centroid is selected.
#
# \param cluster The points of the cluster
# \return One tuple with the centermost point of the cluster
def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)

print "Start..."

full_data = pd.read_csv('/Users/mmfsf/Documents/gitcesar/projeto_portoseguro/poc/dbscan/data/summer-travel-gps-full.csv')
coords = full_data.as_matrix(columns=['lat', 'lon'])

kms_per_radian = 6371.0088
epsilon = 1.5 / kms_per_radian
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

cluster_labels = db.labels_
num_clusters = len(set(cluster_labels))
clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
print('Number of clusters: {}'.format(num_clusters))

centermost_points = clusters.map(get_centermost_point)

lats, lons = zip(*centermost_points)
rep_points = pd.DataFrame({'lon':lons, 'lat':lats})
dbscan_data = rep_points.apply(lambda row: full_data[(full_data['lat']==row['lat']) & (full_data['lon']==row['lon'])].iloc[0], axis=1)
# dbscan_data.to_csv('data/summer-travel-gps-dbscan.csv', encoding='utf-8')
dbscan_data.tail()

# fig, ax = plt.subplots(figsize=[10, 6])
# rs_scatter = ax.scatter(dbscan_data['lon'], dbscan_data['lat'], c='#99cc99', edgecolor='None', alpha=0.7, s=120)
# df_scatter = ax.scatter(full_data['lon'], full_data['lat'], c='k', alpha=0.9, s=3)
# ax.set_title('Full data set vs DBSCAN reduced set')
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.legend([df_scatter, rs_scatter], ['Full set', 'Reduced set'], loc='upper right')
# plt.show()

X = np.radians(coords)
X = StandardScaler().fit_transform(X)

unique_labels = set(cluster_labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (cluster_labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % num_clusters)
plt.show()

print "End."