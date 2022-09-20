num1=int(1)
num2=int(5)
num1=num1+num2
print(num1); 

# num2=100
#if-else version 1
if num1 > num2:
    print('el numero 1 es mayor')
else: 
    print('el numero 2 es mayor')

if num2 > num1:
    print('num2 es mayor')
else:
    if num2 == num1:
        print('son iguales')
    else:
        print('num1 es mayor')

if num2 > num1:
    print('num2 es mayor')
elif num2 == num1:
    print('son iguales')
else:
    print('num1 es mayor')

