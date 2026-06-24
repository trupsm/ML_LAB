import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load Iris dataset
iris = load_iris()
# Create DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)
# Heatmap
sns.heatmap(data.corr(), annot=True)
plt.title("Iris Dataset Heatmap")
plt.show()