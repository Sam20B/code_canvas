for num in range(45, 1050):
    if num % 2 == 0:
        print("fizz")
    if num % 5 ==0:
        print("buzz")
    if num % 10 == 0:
        print("fizzbuzz")
    else:
        print(num)
