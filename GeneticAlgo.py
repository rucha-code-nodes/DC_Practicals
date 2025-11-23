import random

target = "HELLO"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def make():
    return "".join(random.choice(letters) for _ in target)


def change(s):
    s = list(s)
    s[random.randrange(len(s))] = random.choice(letters)
    return "".join(s)

s = make()
gen = 0

while s != target:
    s2 = change(s)
    if sum(a==b for a,b in zip(s2,target)) > sum(a==b for a,b in zip(s,target)):
        s = s2
    gen += 1
    print("Gen", gen, ":", s)

print("\nReached:", s)
#`zip()` simply **pairs elements from two lists one-by-one**, like matching socks together. 🧦😊
