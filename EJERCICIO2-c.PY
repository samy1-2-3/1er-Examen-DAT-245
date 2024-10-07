import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter
import csv

# Cargar el dataset
file_path = 'Student_performance_data _.csv'

# Leer el archivo CSV
data = []
with open(file_path, mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar los encabezados
    for row in lector_csv:
        data.append(row)

# Extraer las columnas relevantes
ethnicity = [int(row[3]) for row in data]  # Columna 'Ethnicity'
parental_education = [int(row[4]) for row in data]  # Columna 'ParentalEducation'
study_time_weekly = [float(row[5]) for row in data]  # Columna 'StudyTimeWeekly'

# Definir función para calcular media, mediana y moda
def calcular_estadisticas(columna, nombre):
    media = np.mean(columna)
    mediana = np.median(columna)
    moda = stats.mode(columna)
    print(f"{nombre} -> Media: {media}, Mediana: {mediana}, Moda: {moda}")
    return media, mediana, moda

# Calcular estadísticas para cada columna
calcular_estadisticas(ethnicity, "Ethnicity")
calcular_estadisticas(parental_education, "ParentalEducation")
calcular_estadisticas(study_time_weekly, "StudyTimeWeekly")

# Gráfico de diagrama de cajas y bigotes (boxplot) para las 3 columnas seleccionadas
plt.figure(figsize=(10, 6))
plt.boxplot([ethnicity, parental_education, study_time_weekly], labels=['Ethnicity', 'ParentalEducation', 'StudyTimeWeekly'])
plt.title('Diagrama de Cajas y Bigotes para Ethnicity, ParentalEducation, y StudyTimeWeekly')
plt.ylabel('Valores')
plt.grid(True)
plt.show()
