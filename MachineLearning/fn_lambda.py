"""
Lambda es una funcion anonima
"""

def doble(x):
    return x*2

print(doble(10))

doble2 = lambda x: x*2
print(doble2(10))

lista = [1,3,65,2,5,8,4,6,67,32,9]
lista_pares = list(filter(lambda x: (x % 2 == 0), lista))
print(lista_pares)

lista2 = [2,3,1,5,6,32,10,23,24,14,56,99,12]
lista_doble = list(map(lambda x: x * 2, lista2))
print(lista_doble)