def mult(n):
    return n * 5

lista = [1,2,3,4,5,6,7]
lista_map = list((map(mult, lista))) # se recorre mult y lista con map

print(lista_map)

def cursos(c):
    return c.upper()

tupla = ('python', 'js', 'java', 'dart', 'c++')
tupla_update = tuple(map(cursos, tupla))
print(tupla_update)

def impares(n):
    if(n % 2 == 1):
        return n

lista=[1,2,3,4,5,6,7]
lista_impar= list(filter(impares,lista))
print(lista_impar)