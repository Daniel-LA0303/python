import array as ar
import numpy as np

#definiendo matriz
matriz = ar.array('i',[1,2,3,4,5]) #i es el tipo de dato tambien 'f', 'd' etc
print(matriz);

#iteracion con for
for ar in matriz:
    print(ar)

#matriz con numpy
matriz2 = np.array([1,2,3,4,5])
print(matriz2);

#lista
lista = [1,3,5]
matriz3 = np.array([2,4,6]);
print('diferencias entre lista:')
lista.append(7) #agrega el valor 7
print(lista)
print( 'y un array')
print(matriz3)
#no se pueden aplicar op aritmeticas de manera directa en listas
a=[1,2,3]
b=[4,5,6]
#en arrays de numpy si podemos hacer operaciones directas
a1 = np.array([1,2,3])
b1 = np.array([4,5,6])
print(a1*b1)
#con listas se tendran problemas de memoria
#con array de numpy es mas recomendable ya que se usa la memoria de forma dinamica