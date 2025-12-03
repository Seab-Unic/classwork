list = [4, -9, 16, -25]
gen = (x**2 if x > 0 else 0 for x in list)
for x in gen:
    print(x)

