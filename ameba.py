def pnnb(n, b=1):
    if b > n:
        return
    print(f"{b}")
    pnnb(n, b + 1)

n = int(input())
pnnb(n)
