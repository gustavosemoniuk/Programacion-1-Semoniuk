array1 = [0]*5
array2 = [0]*5

for i in range(5):
    array1[i] = int(input(f"Ingrese el elemento {i+1} del primer array: "))

for i in range(5):
    array2[i] = int(input(f"Ingrese el elemento {i+1} del segundo array: "))

iguales = True

for i in range(5):
    if array1[i] != array2[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales.")
else:
    print("Los arrays no son iguales.")
