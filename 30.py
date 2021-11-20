num = int(input("enter your number: "))
power = int(input("power: "))
result=1

while power>=1:
    result=result*num
    power -=1

print("result=> ",result)