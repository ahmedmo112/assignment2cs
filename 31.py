x =int(input('x => '))
y =int(input('y => '))
z =int(input('z => '))

ck = False

if x * y == z:
    print(x,'*',y,'=',z)
    ck =True
if x + y ==z:
    print(x,'+',y,'=',z)
    ck =True

if x % y ==z:
    print(x,'%',y,'=',z)    
    ck =True

if x / y ==z:
    print(x,'/',y,'=',z)
    ck =True

if x - y ==z:
    print(x,'-',y,'=',z)    
    ck =True

if x ** y ==z:
    print(x,'**',y,'=',z)    
    ck =True

if(not ck):
    print('Can\'t solve it')

