import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
X = iris.data
plt.boxplot(X)
plt.title("Box Plot")
plt.show()