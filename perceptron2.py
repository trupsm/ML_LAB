import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def train(X, y):
    w = np.random.rand(2)
    b = np.random.rand()
    for _ in range(100):
        for i in range(len(X)):
            out = sigmoid(np.dot(X[i], w) + b)
            err = y[i] - out
            w += 0.1 * err * X[i]
            b += 0.1 * err
    return w, b
# Input data
X = np.array([[0,0],[0,1],[1,0],[1,1]])
# AND and OR outputs
y_and = np.array([0,0,0,1])
y_or  = np.array([0,1,1,1])
# Train
w1, b1 = train(X, y_and)
w2, b2 = train(X, y_or)
# Predict
#AND GATE 
print("AND Gate")
for x in X:
    print(x, "->", round(sigmoid(np.dot(x, w1) + b1)))
# OR GATE 
print("\nOR Gate")
for x in X:
    print(x, "->", round(sigmoid(np.dot(x, w2) + b2)))