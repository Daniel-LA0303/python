import numpy as np

m = np.random.randint(10, size=(5)) #numero aleatorio, size = elementos
print(m)

m2 = np.random.randint(10, size=(3, 3)) #matriz 3x3 random
print(m2)

m3 = np.random.rand(5) #arreglo con numeros decimales
print(m3)

m4 = np.random.rand(5,5) #matiz con numeros decimales
print(m4)

m5 = np.random.choice([1,2,5,9,23,74,23]) #extrae un valor random dentro del array
print(m5)

m6 = np.random.choice([1,2,5,9,23,74,23], size=(2, 3)) #genera una mtriz con los valores
print(m6)

m7 = np.random.choice([2,4,6], p = [0.5, 0.5, 0.0], size=(3)) #probabilidad de devolver un numero, size=numero de lanzamientos, p=matriz de probabilidad
print(m7)

m8 = np.random.choice([2,4,8,10], p=[0.3, 0.5,0.1, 0,1], size=(50))
print(m8)