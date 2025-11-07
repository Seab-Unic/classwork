def fib(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fib_s = fib(n - 1)
    fib_s.append(fib_s[-1] + fib_s[-2])
    return fib_s

n = int(input())
print(fib(n))
