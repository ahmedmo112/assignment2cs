i = 1
Factorial = 1
x = int(input("x="))
if x > 0:
    while i <= x:
        Factorial = Factorial * i
        i = i + 1

    print(f" The Factorial of the number is {Factorial} ")

else:
    print("invalid input")
