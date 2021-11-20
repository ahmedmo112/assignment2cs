num = input("enter intger: ")


pow = len(num)
sum=0
tmp=0
for i in num:
    #print(i)
    sum= sum +int(i)
    tmp = tmp + int(i)**pow

print("The sum of the digits is ",sum)

if int(num) == tmp:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
