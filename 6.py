arr = [val**2 for val in range(0,50)]

print("the array before swaped =>",arr)
i=0
while i <len(arr):
    tmp =arr[i]
    if i != len(arr)-1:
        arr[i] = arr[i+1]
        arr[i+1] = tmp
    i +=2

print("\n\nthe array After swaped =>",arr)
