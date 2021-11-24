n = int(input("n=> "))
k=1
sum = 0
for i in range(n):
    if i % 2 == 0:
        sum += 1/k
    else:    
        sum -= 1/k
    k += 2
print(sum)