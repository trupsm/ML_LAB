import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load Iris dataset
X = load_iris().data
# Number of clusters
k = int(input("Enter number of clusters: "))
# Initialize first k points as centroids
centroids = X[:k]
for _ in range(100):
    # Calculate distance of every point to every centroid
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    # Assign each point to the nearest centroid
    labels = np.argmin(distances, axis=1)
    # Compute new centroids
    new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    # Stop if centroids do not change
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids
# Display centroids
print("Centroids:")
print(centroids)
# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1],marker='x', color='red', s=200)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()