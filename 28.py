num = int(input("enter intger: "))
pow = len(str(num))
sum=0
tmp=0
x=num
i=0
while i < pow:
    sum += x % 10
    x = x//10
    tmp = tmp+ (num//10**i%10)**pow
    i+=1
print("The sum of the digits is ",sum)
if num == tmp:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
