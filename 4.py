i = 1
fact = 1
x = int(input("x="))
if x > 0:
    while i <= x:
        fact = fact * i
        i += 1

    print(" The factorial of the number is ",fact)

else:
    print("less than 0")
