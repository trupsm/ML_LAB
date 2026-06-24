import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
X = load_iris().data
plt.boxplot(X)
plt.title("Box Plot")
plt.show()