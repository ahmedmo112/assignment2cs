dec = int(input("enter the deciaml number: "))
arr = []
if dec >0 and dec<255:
    while dec != 0:
        arr.append(dec%2)
        dec = dec//2
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end='')
else:
    print("invald input")
       