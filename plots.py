import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_state_value_function(Q):

    V = np.max(Q, axis=-1)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(range(V.shape[1]), range(V.shape[0]))

    ax.plot_wireframe(x, y, V)
    plt.show()


