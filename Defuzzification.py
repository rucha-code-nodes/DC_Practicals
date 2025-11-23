
X  = [1, 2, 3]          
mu = [0.1, 0.6, 0.9]    

def max_membership():
    m = max(mu)                
    i = mu.index(m)            
    return X[i]                


def centroid():
    num = 0
    den = 0
    for x, m in zip(X, mu):
        num += x * m
        den += m
    return num / den


def weighted_average():

    num = sum(x*m for x, m in zip(X, mu))
    den = sum(mu)
    return num / den


print("Max Membership:", max_membership())
print("Centroid:", centroid())
print("Weighted Average:", weighted_average())
