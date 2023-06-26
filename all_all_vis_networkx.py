
import loader
import networkx
from matplotlib import pyplot as plt

graph = loader.load_s1_adj_all_all_nx()

# get an embedding in (x,y) based 
# on adjacency matrix properties.
# This takes some time.
pos = networkx.spectral_layout(graph)

#
fig,ax = plt.subplots(figsize=(8,8), constrained_layout=True)

networkx.draw_networkx(
    graph, 
    pos=pos,
    with_labels=False,
    node_size=10,
    alpha=0.7,
    ax=ax
    )
