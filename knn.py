import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
def calculate_distance(X_train, X_test):
    print("Euclidean Distance:",
          np.linalg.norm(X_train[0] - X_test[0]))
    print("Manhattan Distance:",
          np.sum(np.abs(X_train[0] - X_test[0])))
# Function to train and test KNN
def knn_model(X_train, X_test, y_train, y_test, k, metric):
    knn = KNeighborsClassifier(n_neighbors=k, metric=metric)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    print(f"\n{metric} Distance")
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))
# Load dataset
df = pd.read_csv("glass.csv")
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))
# Features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# Standardize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# User input
k = int(input("Enter the value of k: "))
# Calculate distances
calculate_distance(X_train, X_test)
# Run KNN with both distance metrics
knn_model(X_train, X_test, y_train, y_test, k, "euclidean")
knn_model(X_train, X_test, y_train, y_test, k, "manhattan")