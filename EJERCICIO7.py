import random

numAle = [random.randint(1, 100) for _ in range(10)]
ordenar = sorted(numAle, reverse=True)
funcionX = [(x ** (x * 2)) - 1 for x in numAle]
numAbin = [format(x, '08b') for x in ordenar]

def combinarB(bin1, bin2):
    digitoAle = random.randint(1, 7)
    izquierda = bin1[:digitoAle]
    derecha = bin2[len(bin2) - (8 - digitoAle):]
    nuevoN = izquierda + derecha
    restante1 = bin1[digitoAle:]
    restante2 = bin2[:len(bin2) - (8 - digitoAle)]
    nuevoN2 = restante2 + restante1
    if len(nuevoN2) < 8:
        nuevoN2 = nuevoN2.ljust(8, '0')
    else:
        nuevoN2 = nuevoN2[:8]

    return nuevoN, nuevoN2

nuevosNumeros = []

for i in range(0, len(numAbin), 2):
    if i + 1 < len(numAbin):
        bina1 = numAbin[i]
        bina2 = numAbin[i + 1]
        
        nuevo, sobrante = combinarB(bina1, bina2)
        
        nuevosNumeros.append(nuevo)
        nuevosNumeros.append(sobrante)

digitoAle = random.randint(0, 7)
def mutacion(numbers, index):
    mutar = []
    for number in numbers:
        if number[index] == '1':
            numMutado = number[:index] + '0' + number[index + 1:]
        else:
            numMutado = number[:index] + '1' + number[index + 1:]
        mutar.append(numMutado)
    return mutar

numerosMut = mutacion(nuevosNumeros, digitoAle)
numerosDecimales = [int(binario, 2) for binario in numerosMut]

print("Numeros aleatorios:", numAle)
print("Numeros ordenados de mayor a menor:", ordenar)
print("Numeros ordenados en binario (8 dígitos):", numAbin)
print("\nNumeros combinados y sobrantes intercalados:", nuevosNumeros)
print("Digito cambiado en el indice:", digitoAle)
print("Numeros modificados:", numerosMut)
print("Numeros modificados en decimal:", numerosDecimales)
