result=None
x=int(input("Enter your first number: "))
op=input("Enter the operator and enter the equal sign to exit(+, -, *, /): ")
y=int(input("Enter the second number: "))
if (op=='+'):
    result=x+y
    print(f'The sum of {x} and {y} is {result}\n')
elif (op=='-'):
    result=x-y
    print(f'The difference of {x} and {y} is {result}\n')
elif (op=='*'):
    result=x*y
    print(f'The product of {x} and {y} is {result}\n')
elif (op=='/'):
    result=x/y
    print(f'The quotient of {x} and {y} is {result}\n')
else:
    print('Invalid entry for operator. Please re-input\n')
print('Thank you and goodbye!')
