import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load Iris dataset
iris = load_iris()
X = iris.data
# Select 2 features
x = X[:, 2]  # Petal Length
y = X[:, 3]  # Petal Width
# Create grid
xg = np.linspace(x.min(), x.max(), 100)
yg = np.linspace(y.min(), y.max(), 100)
Xg, Yg = np.meshgrid(xg, yg)
# Sample function for contour levels
Z = Xg**2 + Yg**2
# Draw contour plot
plt.contour(Xg, Yg, Z, 10)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Contour Plot of Iris Features")
plt.show()