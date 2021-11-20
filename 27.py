num = int(input("enter intger: "))

sum=0
while num!=0:
    sum += num % 10
    num = num//10

print("The sum of the digits is ",sum)
