#Ejercicio 1: Registro de Temperaturas
#Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
#Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#    El promedio de temperatura de cada día.
#    El promedio general de toda la semana.

from modulos import cargar_datos, mostrar_datos, promedio_dias, promedio_semana

datos = [[0,0,0,],  #Fila = dia, Columna = horario
         [0,0,0,], 
         [0,0,0,],
         [0,0,0,],
         [0,0,0,],
         [0,0,0,],
         [0,0,0,],
         ]

FILAS = 7
COLUMNAS = 3

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
horario = ["Mañana", "Tarde", "Noche"]

while True:
    print("Menu Estacion Metereologica")
    print("1. Cargar")
    print("2. Mostrar")
    print("3. Promedio Dias")
    print("4. Promedio Semana")
    print("5. Salir")

    opcion = input("Seleccione una Opcion: ")

    if opcion == "1":
        cargar_datos(datos,dias,horario)
    elif opcion == "2":
        mostrar_datos(datos,dias,horario)
    elif opcion == "3":
        promedio_dias(datos,dias,horario)
    elif opcion == "4":
        promedio = promedio_semana(datos,dias,horario)
        print(f"El Promedio de la Semana es: {promedio} °C")
    elif opcion == "5":
        break
