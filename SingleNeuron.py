import matplotlib.pyplot as plt

X = [1,2,3,4]
Y = [20,40,60,80]

w=b=0
lr=0.01

for i in range(500):
  for x,y in zip(X,Y):
    y_pred = w*x+b
    error = y-y_pred
    w += error*lr*x
    b += error*lr


print("W: ", w)
print("B: ", b)
print("Score for 5 hours: ", w*5+b)

plt.scatter(X,Y,color="pink",label='Training Data')
plt.plot(X, [w*x+b for x in X], color="black",label='Regreesion  Line')

plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Graph")
plt.legend()
plt.show()