from typing import TextIO
from flask import jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv(r'C:\Users\arons\OneDrive\Escritorio\EscuelaApi\ista-python-curso-2022\baseDatos\asistencia.csv')

print(df.info())
#Este nos mostrara los 10 primeros registros
print(df.head(10))
#Este nos mostrar los datos que yo quiera mostrar en cada en una de mis variables
print(df['cedula'].head(10))
#Este nos mostrara la variable estadistica de nuestros datos numericos
print(df.describe())

#----------------------Estudiante------------------

df2 = pd.read_csv(r'C:\Users\arons\OneDrive\Escritorio\EscuelaApi\ista-python-curso-2022\baseDatos\estudiante.csv')

print(df2.info())
#Este nos mostrara los 10 primeros registros
print(df2.head(10))
#Este nos mostrar los datos que yo quiera mostrar en cada en una de mis variables
print(df2['cedula'].head(10))
#Este nos mostrara el nombre
print(df2['primer_nombre'].head(10))
#Este nos mostrara la variable estadistica de nuestros datos numericos
print(df2.describe())

asistencia_completa = df2['primer_nombre'].head(10), df2['segundo_nombre'].head(10),  df['fecha_dia'].head(10) 

print(asistencia_completa)


#----------Falta practica para matlab
fig, ax = plt.subplots()

dias = [df['fecha_dia'].head(10)]

nombres = [df2['primer_nombre'][0]]

ax.plot(dias, nombres[0])

plt.show()





