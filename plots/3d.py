import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
X = load_iris().data
x = X[:, 2]
y = X[:, 3]
Xg, Yg = np.meshgrid(
    np.linspace(np.min(x), np.max(x), 50),
    np.linspace(np.min(y), np.max(y), 50)
)
Z = np.sin(Xg) * np.cos(Yg)
ax = plt.axes(projection='3d')
ax.plot_surface(Xg, Yg, Z)
plt.title("3D Surface Plot")
plt.show()