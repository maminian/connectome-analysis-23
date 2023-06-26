
import loader
from matplotlib import pyplot as plt
from sklearn import cluster
import numpy as np


# graph with 2952 vertices
# looks like it's sparse (many zeros)
df = loader.load_s1_adj_all_all()

A = df.values

# spectral clustering 
# (attempt to reorder numbering to reveal
# groups of related nodes in the graph)
#
# following 
# https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering-graphs
#

nclusters = 3 # chosen arbitrarily for now
sc = cluster.SpectralClustering(nclusters, affinity='precomputed', assign_labels='discretize')
cluster_labels = sc.fit_predict(A)

order = np.argsort(cluster_labels) # ordering of vertices to group by cluster label

A2 = A[order]
A2 = A2[:,order]

#

#
# Visualize original adjacency as 
# well as the clustering.
#

fig,ax = plt.subplots(1,2, figsize=(10,5), sharex=True, sharey=True, constrained_layout=True)

# TODO: too sparse to see anything in the 
# adjacency. Individual values can be seen 
# if one zooms in to the upper left corner 
# (e.g. A2's upper 5-by-5 block has nonzero values)
ax[0].pcolor(A, cmap=plt.cm.Greys_r)
ax[1].pcolor(A2, cmap=plt.cm.Greys_r)

fig.show()
