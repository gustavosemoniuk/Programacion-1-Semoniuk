numeros = [0,0,0,0,0,0]

for i in range(6):
    numeros[i] = int(input("Ingrese un número entero: "))

print("lista invertida:")
for i in range(5, -1, -1):
    print(numeros[i])
