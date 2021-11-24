x = input('enter string: ')
def digitAndLetters(x):
    dig=0
    let = 0
    for i in x:
        if i != '.':
            if i.isdigit():
                dig +=1
            elif i.isalpha() :
                let +=1
    print('letter  ',let)
    print('digits  ',dig)
digitAndLetters(x)