import numpy as np

vector = np.array([1,2,3,4,5,6])
print(vector)

#definiendo matriz
matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)

lista = [1,2,3,4,5]
matriz2 = np.array(lista) #hacemos disponible los valores de la lista en una matriz
print(matriz2)

lista2 = [[1,2,3], [4,5,6],[7,8,9]]
matriz3 = np.array(lista2)
print(matriz3)

matriz4 = np.arange(15).reshape(3,5) #15 =n cantidad dentro de nuestra matriz, 3= filas, 5=col
print(matriz4)
print(matriz4.shape) #shape para saber col y fi
print(matriz4.ndim) #numero de dimensiones
print(matriz4.size) #tamaño de la matriz

matriz5 = np.zeros((4,5)) #genera matriz de 0
print(matriz5)

matriz6 = np.linspace(99, 88, 25) #genera un matriz entre 99 y 88 con 25 valores
print(matriz6)

#matriz 3d
matriz7 = np.arange(24).reshape(2, 3, 4) #genera una matriz 3d, 2=matrices, 3=filas, 4=cols
print(matriz7)
