#usar un data frame a partir de un archivo excel o csv
import pandas as pd

"""
Un dataset es un conjunto de datos tabulados en cualquier sistema de almacenamiento de datos estructurados
"""
#llamando a nuestro archivo .csv
df = pd.read_csv('ModalidadVirtual.csv')
#buscando campo especifico
print(df['carrera'][1])

#rango a partir de la edad
print(df['edad'] > 23)

#filtrando datos para mostrar todos los resultados de todos los CAMPOS
filtrar = df['edad'] > 23
df_filtrar= df[filtrar]
print(df_filtrar)

#funciones de dataFrame
#muestra primeras 10 filas
print(df.head(10))
#muestra las utimas n filas
print(df.tail(10))