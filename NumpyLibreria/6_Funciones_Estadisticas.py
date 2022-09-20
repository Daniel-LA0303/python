import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print("")
print(np.amax(m)) #numero mayor de la matriz
print(np.amin(m)) #numero menor de la matriz

print(np.amin(m, 1)) #numeros menor sobre cada fila
print(np.amin(m, 0)) #numeros menor sobre cada col

#rango de una matriz
print(np.ptp(m))

#rango sobre eje
print(np.ptp(m, axis=1))

#percentiles
print(np.percentile(m, 50))
print(np.percentile(m, 50, axis=1) ) #percentil sobre eje}

#mediana
print(np.median(m))
print(np.median(m, axis=0)) #mediana sobre eje 0

#media aritmetica
print(np.mean(m))
print(np.mean(m, axis=1)) #media aritmetica sobre eje 1

m2=np.array([1,2,3,4,5,6])
#promedio pongrado
print(np.average(m2))

#desviacion estandar
print(np.std(m2))