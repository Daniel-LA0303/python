import pandas as pd
df = pd.read_csv('estudiantes.csv')
print(df)

#convertir excel a archivo .csv
convertir = pd.read_excel('estudiantesExcel.xlsx')
convertir.to_csv('nuevo_nombre.csv', index=None, header=True)

#convertir de excel a .csv

