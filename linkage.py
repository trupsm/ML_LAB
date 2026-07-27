import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris
# Load Iris Dataset
iris = load_iris()
# Take first 6 samples for simplicity
data = iris.data[:6]
# Function to calculate proximity matrix
def proximity_matrix(data):
    n = len(data)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            # Euclidean Distance
            distance = np.linalg.norm(data[i] - data[j])
            matrix[i][j] = distance
            matrix[j][i] = distance
    return matrix
# Function to plot dendrogram
def plot_dendrogram(data, method):
    # Perform hierarchical clustering
    linkage_matrix = linkage(data, method=method)
    # Draw dendrogram
    dendrogram(linkage_matrix)
    plt.title(f"{method} Linkage")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.show()
# Display Proximity Matrix
print("Proximity Matrix:")
print(proximity_matrix(data))
# Single Linkage Dendrogram
plot_dendrogram(data, "single")
# Complete Linkage Dendrogram
plot_dendrogram(data, "complete")