list = [10, 30, 60, 5, 45]
gen = ("High" if x > 50 else "Medium" if 20 <= x <= 50 else "Low" for x in list)
for x in gen:
    print(x)

