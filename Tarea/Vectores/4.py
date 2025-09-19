numeros = [0]*8

mayores = 0

for i in range(8):
    numeros[i] = int(input("Ingrese un numero: "))
    if numeros[i] > 100:
        mayores = mayores + 1
print("La cantidad de numeros mayores a 100 es:", mayores)