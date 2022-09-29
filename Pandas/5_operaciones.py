import pandas as pd

df = pd.read_csv('estudiantes.csv')
print(df)

#retorna el valor buscado
#print(df.iloc[1,3])
#print(df.iloc[2,3])
#print(df.iloc[2,:3]) #trae toda la fila hasta la col 3

"""Revisar problemas!!!"""
#print(df.loc[3,'EDAD','CARRERA'])

#añadir columnas a data frame
#df['TURNO'] = pd.Series(['tarde','noche','tarde','matutino','noche','matutino','tarde','matutino'])
#print(df)

#elimnar columnas
#SEMESTRE= df.pop('SEMESTRE')
#print(df)

#añadir filas
df = df.append(pd.Series(['nuevo', 1, 'M', 'nuevo' , 'nuevo'],
                         index=['NOMBRE', 'EDAD', 'GENERO','CARRERA', 'TURNO']
                         ), ignore_index=True)
print(df)

#eliminar filas
#df = df.drop([1, 2])
#print(df)


#filtrado de las filas
print("")
df = df[(df['GENERO']=='F') & (df['EDAD'] >= 22)]
#print(df)

#orden de forma alfabetica
#print(df)

#excluye datos que contengan algun campo vacio
df = df.dropna()
print(df)