numeros = [0.0]*6

for i in range(6):
    numeros[i] = float(input("Ingrese un numero: "))

suma = 0.0
for i in range(6):
    suma = suma + numeros[i]
promedio = suma / 6
print("El promedio de los numeros ingresados es:", promedio)