from modulos import cargar_puntajes, mostrar_puntajes, equipo_ganador
#Ejercicio 2: Puntajes de un Torneo
#En un torneo de programación hay 4 equipos que compiten en 5 rondas.
#Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#    El puntaje total de cada equipo.
#   Qué equipo obtuvo el mayor puntaje en total.
FILAS = 4
COLUMNAS = 5
puntajes = [[0, 0, 0, 0 ,0] for _ in range(FILAS)]

cargar_puntajes(puntajes)
mostrar_puntajes(puntajes)
equipo_ganador(puntajes)