import numpy as np

m = np.array([[0,1,2],[4,2,3]])
print(m)
#axis = eje
print(np.sum(m, axis=0)) #hace una suma en el eje 0
print(np.sum(m, axis=1)) #hace una suma en el eje 1

m2 = np.array([[1,1],[1,1]])
m3 = np.array([[8,8],[8,8]])
print(np.concatenate([m2,m3], axis=0)) #une la dos matrices y los alinea con el eje 0
print(np.concatenate([m2,m3], axis=1)) #une la dos matrices y los alinea con el eje 1

#axis no funciona con el eje 1 cuando concatenamos matrices de una dimension, debe ser axis=0