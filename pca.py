import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
# Plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA on Iris Dataset")
plt.show()