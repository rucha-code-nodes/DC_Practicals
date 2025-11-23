import math


def rbf(x, c):
    return math.exp(-((x - c)**2))


inputs = [0, 1]
targets = [0, 1]


centers = [0, 1]   
weights = [0.2, 0.8]  


def rbf_network(x):
    h1 = rbf(x, centers[0])  
    h2 = rbf(x, centers[1])  
    y = h1*weights[0] + h2*weights[1]  
    return round(y, 3)


print("RBF Network Output")
for i in range(len(inputs)):
    print(f"Input: {inputs[i]}  --> Output: {rbf_network(inputs[i])}")
