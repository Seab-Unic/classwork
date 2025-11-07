def r(a, b):
    if a > b:
        return
    print(f"{a}")
    r(a + 1, b)
a = int(input())
b = int(input())
r(a, b)
