def s(n):
    if n == 1:
        return "да"
    if n <= 0 or n % 2 != 0:
        return "нет"
    return s(n // 2)
n = int(input())
print(s(n))
