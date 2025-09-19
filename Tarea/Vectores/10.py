from funcion10 import primera_aparicion

numeros = [0]*5
for i in range(5):
    numeros[i] = int(input("Ingrese un numero: "))

buscar = int(input("Ingrese un numero a buscar: "))

posicion = primera_aparicion(numeros, buscar)

if posicion != -1:
    print("El numero se encuentra en la posicion:", posicion + 1)  
else:
    print("El numero no se encuentra en el array.")