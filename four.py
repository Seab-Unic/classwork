import random
n = random.randint(5,15)
d = {i: "even" if i % 2 == 0 else "odd" for i in range(1, n + 1)}
print(d)
