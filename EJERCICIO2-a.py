import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/samy1-2-3/1er-Examen-DAT-245/refs/heads/main/Student_performance_data%20_.csv'
datos = pd.read_csv(url)

def percentil(columna, percentil):
    ordenados = sorted(columna)
    n = len(ordenados)
    k = (n - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < n:
        return ordenados[f] + c * (ordenados[f + 1] - ordenados[f])
    else:
        return ordenados[f]

def cuartil(columna):
    Q1 = percentil(columna, 25)
    Q2 = percentil(columna, 50)  
    Q3 = percentil(columna, 75)
    return Q1, Q2, Q3


for columna in datos.select_dtypes(include='number').columns:
    print(f'Columna: {columna}')
    Q1, Q2, Q3 = cuartil(datos[columna].dropna())
    print(f'Cuartil 1 (Q1): {Q1}')
    print(f'Cuartil 2 (Mediana): {Q2}')
    print(f'Cuartil 3 (Q3): {Q3}')
    print(f'Percentil 90: {percentil(datos[columna].dropna(), 90)}')
    print('---')

for columna in datos.select_dtypes(include='number').columns:
    plt.figure(figsize=(8, 6))
    plt.hist(datos[columna].dropna(), bins=20, edgecolor='black', alpha=0.7)
    plt.title(f'Distribucion de la columna {columna}')
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

