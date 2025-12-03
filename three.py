list = [5, 12, 8, 20, 3, 15]
gen = (x if x > 10 else 0 for x in list)
for x in gen:
    print(x)
