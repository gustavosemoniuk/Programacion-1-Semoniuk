from modulos import cargar_productos, total_producto, total_dia, mayor_produccion
#Ejercicio 3: Control de Producción
#Una fábrica produce 3 productos y mide la producción durante 4 días.
#Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#    La producción total de cada producto.
#    La producción total de cada día.
#    Cuál fue el día con mayor producción total.

FILAS = 3
COLUMNAS = 4

produccion = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

cargar_productos(produccion)
total_producto(produccion)
total_dia(produccion)
mayor_produccion(produccion)

