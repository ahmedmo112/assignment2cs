str = input('input string => ')
n = int(input('n => '))
if n <len(str):
    print(str.replace(str[n],''))
else:
    print('n  is bigger than the string indexis')
