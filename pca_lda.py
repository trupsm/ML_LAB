import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
iris=load_iris()
target=iris.target
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df=df.drop_duplicates()
df=df.fillna(df.mean())
X=df.values
y=target[:len(df)]

pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)

plt.figure(figsize=(6,4))
plt.scatter(X_pca[:,0],X_pca[:,1],c=y)
plt.title("PCA ")
plt.show()

lda=LDA(n_components=2)
X_lda=lda.fit_transform(X,y)
plt.figure(figsize=(6,4))
plt.scatter(X_lda[:,0],X_lda[:,1],c=y)
plt.title("LDA ")
plt.show()