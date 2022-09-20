num1=int(1)
num2=int(5)
booleano=False

if(True):
    num2=10
    print(num2)
if(not booleano):
    num1=15
    print(num1)

#operadores
"""
opreadores logiocos
1.- not
2.- and
3.- or

operadores de pertenencia
1.- in
2.- not in
"buen" in "este es un buen ejemplo"
True
"buen" not in "este es un buen ejemplo"
False

operadores de identidad
1.- is
2.- is not
>>> a = "hola"
>>> b = a
>>> b is a
True
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
"""

#ejercicio 1
#calcular el area de untriangulo
"""
b = base
h = altura
area = (b*h)/2
"""
b= int(input('ingrese la base: '))
h= int(input('ingrese la altura: '))
area=(b*h)/2
print(area)

#ejercicio2
#promedio
n=int(input('ingrese nota 1:'))
n2=int(input('ingrese nota 2:'))
n3=int(input('ingrese nota 3:'))
promedio=float((n+n2+n3)/3)
print(promedio)

#operadores relaionales
# <, >, >=, <=, =, ==

#operadores logicos
#and, or, not, 