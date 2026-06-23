import numpy as np
def step(x):
    return 1 if x >= 0 else 0
X = np.array([[0,0],[0,1],[1,0],[1,1]])

# AND Gate
w = np.array([1,1])
b = -1.5
print("AND Gate")
for x in X:
    print(x, "->", step(np.dot(x,w)+b))

# OR Gate
w = np.array([1,1])
b = -0.5
print("\nOR Gate")
for x in X:
    print(x, "->", step(np.dot(x,w)+b))
