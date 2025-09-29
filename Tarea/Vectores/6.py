numeros = [0]*7

for i in range(7):
    numeros[i] = int(input("Ingrese un número entero: "))

mayor = numeros[0]
posicion = 0

for i in range(1,7):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i + 1

print("El número mayor es:", mayor)
print("Se encuentra en la posición:", posicion)
