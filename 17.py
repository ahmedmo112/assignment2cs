dec = int(input("enter the deciaml number: "))

if dec >0 and dec<255:
    while dec != 0:
        print(dec%2,end='')
        dec = dec//2
else:
    print("invald input")
    
print('\n')       