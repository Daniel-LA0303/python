import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('catalogo-de-sismos.csv') #leyendo datos

sismosData = pd.DataFrame(df) #asignando datFrame

sismosData = sismosData.sort_values('year') #orden por año



#Latitud

x_valores_años = sismosData['year'].tolist()

y_valores_l = sismosData['latitud'].tolist()

y_valores_m = sismosData['magnitud'].tolist()

y_valores_p = sismosData['profundida'].tolist()
"""
plt.figure(figsize=(15, 6)) #cambia el tamaño de la fig
plt.plot(x_valores_años, y_valores_l, marker='o', linestyle='--')
plt.xlabel('Años') #agrega label eje x
plt.ylabel('Latitud') #agrega label eje y
plt.title('Latitud reflejada en años') #agrega titulo
plt.show()
"""
#Magnitud

"""
plt.figure(figsize=(15, 6)) #cambia el tamaño de la fig
plt.plot(x_valores_años, y_valores_m, marker='o', linestyle='--', color='g', label='magnitud')
plt.xlabel('Años') #agrega label eje x
plt.ylabel('Magnitud') #agrega label eje y
plt.title('Magnitud reflejada en años') #agrega titulo
plt.show()
"""

#suplot
"""
fig, ax = plt.subplots(1, 2, sharey=True) #figura
ax[0].plot(x_valores_años, y_valores_m, color='r', label='Magnitud')#valores primer subplot
ax[0].legend()
ax[1].plot(x_valores_años, y_valores_p, color='g', label='Profundidad')#valores segundo subplot
ax[1].legend()
plt.show()                                
"""

#Promedios profundidad, latitud, magnitud
promedio_P = np.average(y_valores_p)
promedio_L = np.average(y_valores_l)
promedio_M = np.average(y_valores_m)

x_barra = ['Profundidad', 'Latitud', 'Magnitud']
y_barra = [promedio_P, promedio_L, promedio_M]
plt.bar(x_barra, y_barra)
plt.title('Promedios de profundidad, latitud y magnitud entre 1994 y 2018') #agrega titulo
plt.show()
