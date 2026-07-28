import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv("glass.csv")
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
def knn(metric):
    model = KNeighborsClassifier(n_neighbors=3, metric=metric)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nDistance:", metric)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
knn("euclidean")
knn("manhattan")