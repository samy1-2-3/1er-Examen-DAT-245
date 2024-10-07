import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

matriz = []
with open('Student_performance_data _.csv', mode='r') as archivo:
    leer = csv.reader(archivo)
    for fila in leer:
        matriz.append(fila)


encabezados = matriz[0]
datos = []
for fila in matriz[1:]:
    filaN = []
    for valor in fila:
        try:
            filaN.append(float(valor))
        except ValueError:
            filaN.append(valor) 
    datos.append(filaN)

columnas3 = ['Ethnicity', 'ParentalEducation', 'StudyTimeWeekly']
indiceCol = [encabezados.index(col) for col in columnas3]
datosCol = [[fila[idx] for fila in datos] for idx in indiceCol]

Ethnicity = np.array(datosCol[0], dtype=float)
ParentalEducation = np.array(datosCol[1], dtype=float)
StudyTimeWeekly = np.array(datosCol[2], dtype=float)


def caracteristicas(columna, nombreCol):
    media = np.mean(columna)
    desvEstandar = np.std(columna)
    maximo = np.max(columna)
    minimo = np.min(columna)
    moda = stats.mode(columna)
    print(f"\nCaracteristicas de {nombreCol}:")
    print(f"Media: {media}")
    print(f"Desviación estándar: {desvEstandar}")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
    print(f"Moda: {moda}")


caracteristicas(Ethnicity, 'Ethnicity')
caracteristicas(ParentalEducation, 'ParentalEducation')
caracteristicas(StudyTimeWeekly, 'StudyTimeWeekly')

plt.hist(Ethnicity, bins=10, color='blue', alpha=0.7)
plt.title('Distribución de Ethnicity')
plt.xlabel('Ethnicity')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(ParentalEducation, bins=10, color='orange', alpha=0.7)
plt.title('Distribución de ParentalEducation')
plt.xlabel('ParentalEducation')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(StudyTimeWeekly, bins=10, color='green', alpha=0.7)
plt.title('Distribución de StudyTimeWeekly')
plt.xlabel('StudyTimeWeekly')
plt.ylabel('Frecuencia')
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot([Ethnicity, ParentalEducation, StudyTimeWeekly], labels=['Ethnicity', 'ParentalEducation', 'StudyTimeWeekly'])
plt.title('Boxplot de Ethnicity, ParentalEducation y StudyTimeWeekly')
plt.ylabel('Valores')
plt.show()
