def mostrar_atracciones():
    print("Menu de Atracciones")
    print("1. Montaña Rusa")
    print("2. Carrusel")
    print("3. Casa del Terror")
    seleccion_atracciones = int(input("Enumere cuántas atracciones desea visitar: "))
    atracciones = ""
    for i in range(seleccion_atracciones):
        atraccion = int(input(f"Seleccione la atracción a visitar {i+1}: "))
        atracciones += str(atraccion)
    return atracciones
 
def puede_subir(edad:int, atraccion:int):
    if  edad < 6:
        return atraccion == 2
    elif atraccion == 1 and edad < 12:
        return False
    else:
        return True
 #1 montana, 2 carrusel, 3 casa del terror

def calcular_precio(atraccion:int):
    # precios 1500 = 1, 1200 = 2, 800 = 3
    precio_total = 0
    if atraccion == 1:
        precio_total += 1500
    elif atraccion == 2:
        precio_total += 1200
    elif atraccion == 3:
        precio_total += 800
    return int(precio_total)


def registrar_visita(nombre:str, edad:int):
    nombre = str(input("Por favor, ingresa tu nombre: "))
    edad = int(input("Por favor, ingresa tu edad: "))
    return nombre, edad 

def mostrar_resumen(nombre:str, edad:int, atracciones:str):
    print("Resumen de la Visita")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Atracciones visitadas: {atracciones}")
   
    
  
