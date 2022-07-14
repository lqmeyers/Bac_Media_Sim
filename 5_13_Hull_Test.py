import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

p = [(1,1), (2,1.6), (0.8,2.7), (1.7,3.2)]
p2 = [(0.7,1.3),(2,0.9),(1.4,1.5),(1.9,3.1),(0.6,2.5),(1.4,2.3)]

def convexhull(p):
    p = np.array(p)
    hull = ConvexHull(p)
    return p[hull.vertices,:]

def ccw_sort(p):
    p = np.array(p)
    mean = np.mean(p,axis=0)
    d = p-mean
    s = np.arctan2(d[:,0], d[:,1])
    return p[np.argsort(s),:]

fig, axes = plt.subplots(ncols=3, nrows=2, sharex=True, sharey=True)

axes[0,0].set_title("original")
poly = plt.Polygon(p, ec="k")
axes[0,0].add_patch(poly)

poly2 = plt.Polygon(p2, ec="k")
axes[1,0].add_patch(poly2)

axes[0,1].set_title("convex hull")
poly = plt.Polygon(convexhull(p), ec="k")
axes[0,1].add_patch(poly)

poly2 = plt.Polygon(convexhull(p2), ec="k")
axes[1,1].add_patch(poly2)

axes[0,2].set_title("ccw sort")
poly = plt.Polygon(ccw_sort(p), ec="k")
axes[0,2].add_patch(poly)

poly2 = plt.Polygon(ccw_sort(p2), ec="k")
axes[1,2].add_patch(poly2)


for ax in axes[0,:]:
    x,y = zip(*p)
    ax.scatter(x,y, color="k", alpha=0.6, zorder=3)
for ax in axes[1,:]:
    x,y = zip(*p2)
    ax.scatter(x,y, color="k", alpha=0.6, zorder=3)


axes[0,0].margins(0.1)
axes[0,0].relim()
axes[0,0].autoscale_view()
plt.show()