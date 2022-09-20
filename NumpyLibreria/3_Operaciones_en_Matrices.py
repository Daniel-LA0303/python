import numpy as np
matriz = np.arange(24).reshape(4,6)
print(matriz[3,4]) #busca el elemneto segun la ubicaion

arreglo1 = np.array([1,4,5,2])
print(np.sort(arreglo1)) #ordena el arreglo

arreglo2 = np.array([2,3,4])
print(np.power(arreglo2,3)) #eleva a la n potencia


arreglo3 = np.array([2,3,4,9,5,8])
print(np.array(arreglo3 >= 4)) #condicion

arreglo4 = np.array([2,3,4,9,5,8])
arreglo5 = np.array([10,11,15,17])
print(np.concatenate((arreglo4,arreglo5))) #concatena dos vectores

matriz2 = np.array([[1,2], [3,4]])
matriz3 = np.array([[5,6], [7,8]])
print(matriz2+matriz3) #concatena matrices
print(matriz2 + 2) #le suma el valor de 2 a la matriz 2
print(np.add(matriz2, matriz3)) #otra manera de sumar matrices
print(np.divide(matriz2,matriz3)) #divide las matrices}
print(matriz2.dot(matriz3)) #multiplica las matrices