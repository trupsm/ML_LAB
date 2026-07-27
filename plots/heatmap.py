import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
data = load_iris(as_frame=True).frame
sns.heatmap(data.corr(), annot=True)
plt.title("Heatmap plot ")
plt.show()