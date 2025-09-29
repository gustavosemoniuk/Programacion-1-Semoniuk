# Ingresar datos, 3 listas, mostrar listas, ordenarlos por bubble sort, salir
from funciones import *

nombres = [""]*10
puntuaciones = [0]*10
comentarios = [""]*10

while True:
    print("---Menu de Satisfaccion---")
    print("1. Cargar Datos")
    print("2. Mostrar Datos")
    print("3. Ordenar por puntuacion")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opcion (1-4): "))

    if opcion == 1:
        cargar_datos(nombres, puntuaciones, comentarios)
    elif opcion == 2:
        mostrar_datos(nombres, puntuaciones, comentarios)
    elif opcion == 3:
        ordenar_datos(nombres, puntuaciones, comentarios)
    elif opcion == 4:
        break
    else:
        print("Opcion Incorrecta, Intente Nuevamente.")
    