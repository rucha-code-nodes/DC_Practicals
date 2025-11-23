

import math


x = 0.0
y = 1.0   # expected output


w1 = 0.5   
w2 = 0.1   
lr = 0.1  

def sigmoid(z):
    return 1/(1+math.exp(-z))


for _ in range(5):
    # Forward Pass
    h = sigmoid(x*w1)      
    o = sigmoid(h*w2)    

    # Error
    error = y - o

 
    w2 += lr * error * o*(1-o) * h
    w1 += lr * error * o*(1-o) * w2 * x

    print("Output:", round(o,4), " Error:", round(error,4))

print("\nFinal Weights:", round(w1,3), round(w2,3))
