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
    labels = []
    # Assign each point to nearest centroid
    for point in X:
        distances = []
        for centroid in centroids:
            distances.append(np.linalg.norm(point - centroid))
        labels.append(np.argmin(distances))
    labels = np.array(labels)
    # Compute new centroids
    new_centroids = []
    for i in range(k):
        new_centroids.append(X[labels == i].mean(axis=0))
    new_centroids = np.array(new_centroids)
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
plt.scatter(centroids[:, 0],centroids[:, 1],marker='x',s=200, color='red')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()