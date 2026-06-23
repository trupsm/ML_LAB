import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# Load Glass Dataset
df = pd.read_csv("glass.csv")
# Features and Target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# 70-30 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Euclidean Distance
knn1 = KNeighborsClassifier(n_neighbors=3,metric='euclidean')
knn1.fit(X_train, y_train)
pred1 = knn1.predict(X_test)
print("Euclidean Distance")
print("Accuracy:", accuracy_score(y_test, pred1))
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred1))
# Manhattan Distance
knn2 = KNeighborsClassifier(n_neighbors=3,metric='manhattan')
knn2.fit(X_train, y_train)
pred2 = knn2.predict(X_test)
print("\nManhattan Distance")
print("Accuracy:", accuracy_score(y_test, pred2))
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred2))