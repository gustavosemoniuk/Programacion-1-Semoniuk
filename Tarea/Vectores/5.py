numeros = [0]*10

for i in range(10):
    numeros[i] = int(input("Ingrese un número entero: "))

buscar = int(input("Ingrese el número que desea buscar: "))

encontrado = False
posicion = 01

for i in range(10):
    if numeros[i] == buscar:
        encontrado = True
        posicion = i + 1
        break

if encontrado:
    print("El número se encuentra en la posición:", posicion)
else:
    print("El número no se encuentra en el array.")
