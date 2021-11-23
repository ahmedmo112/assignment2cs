size = int(input("enter array size: "))
A  = [0]* size
for i in range(size):
    A[i]= input(f"enter element {i}: ")
print(A)
p = int(input("enter index where you want the element to be removed: "))

if 0<= p<size:
    A = A[:p]+A[p+1:]
    print(A)
else:
    print("Error")
    

