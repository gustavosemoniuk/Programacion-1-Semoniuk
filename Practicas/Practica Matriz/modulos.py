
def cargar_datos(mat, dias, horario):
    FILAS = len(dias)
    COLUMNAS = len(horario)
    for i in range(FILAS):
        print(f"Temperatura de {dias[i]}")
        for j in range(COLUMNAS):
            temperatura = int(input(f"Ingrese la temperatura de la {horario[j]}: "))
            mat[i][j] = temperatura

def mostrar_datos(mat, dias, horario):
    FILAS = len(dias)
    COLUMNAS = len(horario)

    print("Temperaturas Registradas")
    for i in range(FILAS):
        print(f"{dias[i]}")
        for j in range(COLUMNAS):
             print(f"{horario[j]}: {mat[i][j]} °C")

def promedio_dias(mat, dias, horario):
    FILAS = len(dias)
    COLUMNAS = len(horario)
    
    for i in range(FILAS):
        promedio_dia = sum(mat[i]) // COLUMNAS
        print(f"El promedio de los dias es: {promedio_dia} °C")
   
def promedio_semana(mat, dias, horario):
    total = 0
    FILAS = len(dias)
    COLUMNAS = len(horario)

    for i in range(FILAS):
        total += sum(mat[i])
    
    promedio = total // (FILAS * COLUMNAS)
    return promedio

#///////////////////////////////////////////#

def cargar_puntajes(mat):
    FILAS = 4
    COLUMNAS = 5
    for i in range(FILAS):
        print(f"Equipo {i + 1}")
        for j in range (COLUMNAS):
            puntaje = int(input(f"Cargar los resultados la ronda {j + 1}: "))
            mat[i][j] = puntaje

    

def mostrar_puntajes(mat):
    FILAS = 4
    for i in range(FILAS):
        total = sum(mat[i])
        print(f"El Total del equipo {i+1}: {total}")



def equipo_ganador(mat):
    FILAS = 4
    equipo = 0
    mayor = 0
    for i in range(FILAS):
        total = sum(mat[i])
        if total > mayor:
            mayor = total
            equipo = i + 1

    print(f"El Equipo con mayor puntaje es {equipo} con  {mayor} puntos")

#///////////////////////////////////////////#

def cargar_productos(mat):
    FILAS = 3
    COLUMNAS = 4
    for i in range(FILAS):
        print(f"Produccion del producto {i + 1}")
        for j in range(COLUMNAS):
            datos = int(input(f"Cuanto se produjo en el dia {j+1}: "))
            mat [i][j] = datos

def total_producto(mat):
    FILAS = 3
    for i in range(FILAS):
        total = sum(mat[i])
        print(f"Total producido del Producto {i + 1}: {total}")

def total_dia(mat):
    FILAS= 3
    COLUMNAS = 4
    for j in range(COLUMNAS):
        total_d = sum(mat[i][j] for i in range(FILAS))
        print(f"El total del Día {j + 1} es: {total_d}")

def mayor_produccion(mat):
    FILAS = 3
    COLUMNAS = 4
    mayor = 0
    dia_mayor = 0
    for j in range(COLUMNAS):
        total_m = sum(mat[i][j] for i in range(FILAS))
        if total_m > mayor:
            mayor = total_m
            dia_mayor = j + 1

    print(f"el dia de mayor produccion es: {dia_mayor} con {mayor} Unidades")
