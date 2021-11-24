start = int(input("start: "))
end = int(input("end: "))
for i in range(start,end):
    if i % 9 == 0 and i % 4 != 0:
        print(i,end="")
        if i != end-1:
            print(',',end='')
        else:
           print("")
