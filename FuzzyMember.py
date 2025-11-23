import numpy as np
import matplotlib.pyplot as plt
import math


def triangular(x, a, b, c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)), 0)


def trapezoidal(x, a, b, c, d):
    return max(min((x-a)/(b-a), 1, (d-x)/(d-c)), 0)


def gaussian(x, mean, sigma):
    return math.exp(-((x-mean)**2)/(2*sigma**2))


def gbell(x, a, b, c):
    return 1 / (1 + abs((x-c)/a)**(2*b))


def pi(x, a, b, c, d):
    if x <= a or x >= d: return 0
    elif a < x < b: return 2*((x-a)/(b-a))**2
    elif b <= x <= c: return 1 - 2*((x-c)/(c-b))**2
    else: return 2*((x-d)/(c-d))**2


def gamma(x, a, b):
    if x <= a: return 0
    elif x >= b: return 1
    else: return (x-a)/(b-a)



X = np.linspace(0, 10, 100)

Y1 = [triangular(x, 2, 5, 8) for x in X]
Y2 = [trapezoidal(x, 1, 3, 6, 8) for x in X]
Y3 = [gaussian(x, 5, 1.5) for x in X]
Y4 = [gbell(x, 2, 2, 5) for x in X]
Y5 = [pi(x, 2, 3, 7, 8) for x in X]
Y6 = [gamma(x, 1, 6) for x in X]

plt.plot(X, Y1, label="Triangular")
plt.plot(X, Y2, label="Trapezoidal")
plt.plot(X, Y3, label="Gaussian")
plt.plot(X, Y4, label="G-Bell")
plt.plot(X, Y5, label="Pi")
plt.plot(X, Y6, label="Gamma")

plt.legend()
plt.title("Fuzzy Membership Functions")
plt.show()
