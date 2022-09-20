import numpy as np

m = np.array([[1,-1,2],[3,2,0]])
print(m)

m2 = np.array([[1],[2],[3]])
print(m2)

#transpuesta
print(np.transpose(m2))

#sistema de ecuaciones
A=np.array([[2,1,-2], [3,0,1],[1,1,-1]])
b=np.array([[-3],[5],[-2]])
print(np.transpose(b))
print("")
x = np.linalg.solve(A,b)
print(x)
print(np.allclose(np.dot(A,x),b))

#ejercicio
m3 = np.array([[2,7,3],[2,8,2],[1,3,1]])
print(m3)
m4 = np.array([[1],[1],[0]])
print(m4)

print(np.linalg.solve(m3,m4))