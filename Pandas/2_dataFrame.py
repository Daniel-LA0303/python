import pandas as pd
import numpy as np

data = {'NOMBRE': ['Maria','Jose','David','Ivan'],
        'CARRERA': ['Auditoria','Informatica','Derecho','Idiomas'],
        'CORREO' :['corre1','corre2','corre3','corre4']
        }

estudiantes = pd.DataFrame(data) #creando la dataFrame
print(estudiantes)

#DataFrame a partir de una serie
df = pd.DataFrame([['Maria',27],['David',22],['Ana',24],['Jose',25]], ##Asignamos datos y columnas
                  columns=['NOMBRE','EDAD']
                  )
print(df)

#DataFrme a partir de un array
df2= pd.DataFrame(np.random.rand(4,3), columns=['a','b','c'])
print(df2)
