


## **Code for AND Gate (Simple MP Neuron)**


# AND gate using MP neuron

# inputs
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

# weights and threshold
w1 = 1
w2 = 1
threshold = 2    # neuron fires only if both inputs are 1

print("x1  x2  Output")
for i in range(4):
    total = x1[i]*w1 + x2[i]*w2  # calculate sum
    if total >= threshold:
        print(x1[i], x2[i], "   1")
    else:
        print(x1[i], x2[i], "   0")


##  **Code for OR Gate (Simple MP Neuron)**


# OR gate using MP neuron

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

w1 = 1
w2 = 1
threshold = 1    # neuron fires if ANY input is 1

print("x1  x2  Output")
for i in range(4):
    total = x1[i]*w1 + x2[i]*w2
    if total >= threshold:
        print(x1[i], x2[i], "   1")
    else:
        print(x1[i], x2[i], "   0")


##  **Code for NAND Gate (Simple MP Neuron)**


# NAND gate using MP neuron

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

w1 = -1
w2 = -1
threshold = -1   # gives 0 only for (1,1)

print("x1  x2  Output")
for i in range(4):
    total = x1[i]*w1 + x2[i]*w2
    if total >= threshold:
        print(x1[i], x2[i], "   1")
    else:
        print(x1[i], x2[i], "   0")









# MP Neuron for AND, OR, NOT

def mp_neuron(inputs, threshold):
    return 1 if sum(inputs) >= threshold else 0

# Test AND Gate
print("AND Gate:", mp_neuron([1, 1], 2))  # 1+1 >= 2 → 1

# Test OR Gate
print("OR Gate:", mp_neuron([1, 0], 1))   # 1+0 >= 1 → 1

# Test NOT Gate (special case)
def mp_not(x): 
    return 1 if x == 0 else 0

print("NOT Gate:", mp_not(1))  # 1 → 0


