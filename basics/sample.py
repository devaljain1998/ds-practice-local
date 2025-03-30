import random

# generate list of random integers:
l = [random.randint(0, 100) for i in range(10)]
print("list", l)

s = {n for n in l}
print("set", s)

d = {l[i]:i for i in range(len(l))}
print("dict", d)