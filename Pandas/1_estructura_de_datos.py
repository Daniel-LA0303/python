import pandas as pd
#parte 1
#estructura tipo serie
naranjas = pd.Series([4,9,2,6,10,200]) #definiendo estructura
print(naranjas)

#lista a serie
colores = pd.Series(['rojo','verde', 'amarillo', 'azul', 'morado'])
print(colores)

#diccionario a serie
materias = pd.Series({'Matematicas':60, 'Fisica':100, 'Quimica':78})
print(materias)

#propiedades
numeros = pd.Series([1,2,3,4,5,6,7,8,9])
print(numeros.size)
print(numeros.index)
print(numeros.dtype)

#acceder a una serie
print(colores[1:3]) #recorrido de determinados elementos
print(materias[['Fisica','Quimica']]) #acceder a diccionario
print(numeros*2)

#parte 2
numeros2 = pd.Series([1,2,3,4,5,6,7,8,9])
print(numeros2.sum()) #suma todos los elementos
print(numeros2.std()) #desviacion estandar
print(numeros2.describe())

##Funciones en pandas
serie = pd.Series({'Matematicas':8, 'Economia':6, 'Programacion': 10, 'Fisica':5})
print(serie[serie>6])#extrae los valores mayor que 6
print(serie.sort_values()) #ordena los valores de menor a mayor
print(serie.sort_index(ascending=True)) #ordena los valores de mayor a menor

data = 5
serie2 = pd.Series(data, index=[0,1,2,3,4,5]) #inserta el valor de data en cada campo de la serie
print(serie2)

data_list = ['Nombre 1','Nombre 2','Nombre 3']
indices = ['Equipo1','Equipo2','Equipo3']
equipos = pd.Series(index=indices, data=data_list) #inserta los datos, el indice lo podemos relacionar
print(equipos)
