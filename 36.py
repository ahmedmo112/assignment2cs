x = input('enter string=> ')
# y = ""
# for i in x:
#     y = i + y
# if (x == y):
#     print("palindrome")
# else:
#     print("not palindrome")
if x == x[::-1]:
    print('palindrome')
else:
    print('not palindrome')

