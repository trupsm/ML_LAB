import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
def proximity_matrix(data):
    n = len(data)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distance = np.linalg.norm(data[i] - data[j])
            matrix[i][j] =matrix[j][i]=distance
    return matrix
def plot_dendrogram(data, method):
    plt.figure(figsize=(6, 4))
    dendrogram(linkage(data, method=method))
    plt.title(f"{method} Linkage")
    plt.xlabel("Samples")
    plt.ylabel("Distance")
    plt.show()
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Preprocesing
df = df.drop_duplicates()
df = df.fillna(df.mean())
scaler = StandardScaler()
data = scaler.fit_transform(df)
data = data[:6]

matrix = proximity_matrix(data)
print("Proximity Matrix:")
print(matrix)
plot_dendrogram(data, "single")
plot_dendrogram(data, "complete")