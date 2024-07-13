x = int(input('please enter the input: '))
y = int(input('please enter the another input: '))
ind = str('+ - * / %')
print(ind)
result = str(input('please enter the operation: '))

if result == '+':
    print(x+y)
elif result == '-':
    print(x-y)
elif result == '*':
    print(x*y)
elif result == '/':
    print(x/y)
elif result == '%':
    print(x % y)
else:
    print('invalid input')











