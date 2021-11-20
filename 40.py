size = int(input('enter size: '))

def fibonaccisequence(size):
    i=0
    num1=1
    num2=1
    if size<=0:
        print("Please enter a positive size number")
    else:
        while i<size:
            print(num1)
            tmp = num1+num2
            num1=num2
            num2=tmp
            i +=1

fibonaccisequence(size)