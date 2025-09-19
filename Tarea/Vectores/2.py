numeros = [0]*10

for i in range(10):
    numeros[i] = int(input("Ingrese un numero: "))

suma = 0
for i in range(10):
    suma = suma + numeros[i]
    print("La suma de los numeros ingresados es:", suma)
