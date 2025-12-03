gen = (5 if len(s) > 5 else len(s) for s in lst)
for x in gen:
    print(x)
