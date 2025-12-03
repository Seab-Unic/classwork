fizzbuzz = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else "" for i in range(1, 101)]
result = [x for x in fizzbuzz if x]
print(result)
