import numpy as np

A = [1,0,1, 1,1,1, 1,0,1]
B = [1,1,0, 1,1,1, 1,1,0]
C = [1,1,1, 1,0,0, 1,1,1]

data = np.array([A,B,C])

w = np.random.rand(3,9)

lr = 0.2      
epochs = 20    

for _ in range(epochs):
    for x in data:
        d = np.linalg.norm(w - x, axis=1)
        win = np.argmin(d)
        w[win] = w[win] + lr*(x - w[win])

def test(x):
    d = np.linalg.norm(w - x, axis=1)
    return np.argmin(d)

print("A recognized by neuron:", test(A))
print("B recognized by neuron:", test(B))
print("C recognized by neuron:", test(C))




