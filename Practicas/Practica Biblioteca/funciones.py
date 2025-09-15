MAX = 20
titulos = [""] * MAX
ejemplares = [0] * MAX
cantidad_libros = 0

def menu ():
    global cantidad_libros
    while True:
        print("---Menu Biblioteca---")
        print("1. Cargar Titulos y ejemplares")
        print("2. Mostrar Catalogo")
        print("3. Consultar Disponibilidad")
        print("4. Titulos Agotados")
        print("5. Agregar Titulo")
        print("6. Actualizar Ejemplares")
        print("7. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            cargar_titulos()
        elif opcion == 2:
            f_catalogo()
        elif opcion == 3:
            f_disponibilidad()
        elif opcion == 4:
            titulos_agotados()
        elif opcion == 5:
            agregar_titulo()
        elif opcion == 6:
            actualizar_ejemplares()
        elif opcion == 7:
            break
        else:
            print("Opcion Invalida")

def cargar_titulos():
    global cantidad_libros 
    while cantidad_libros < 20:
        titulo = input("Ingrese el título del libro (o (enter) para terminar): ")
        if titulo == "":
            break
        copias = int(input("Ingrese la cantidad de ejemplares: "))
        titulos[cantidad_libros] = titulo
        ejemplares[cantidad_libros] = copias
        cantidad_libros += 1

def f_catalogo():
    print("Catálogo completo:")
    for i in range(cantidad_libros):
        print(titulos[i], ejemplares[i], "copias")

def f_disponibilidad():
    consulta = input("Título a consultar: ")
    encontrado = False
    for i in range(cantidad_libros):
        if titulos[i] == consulta:
            print("Hay", ejemplares[i], "copias de", titulos[i])
            encontrado = True
    if encontrado == False:
            print("Título no encontrado.")

def titulos_agotados():
    agotados = False
    for i in range(cantidad_libros):
        if ejemplares[i] == 0:
            print(titulos[i])
            agotados = True
    if agotados == False:
        print("No hay títulos agotados.")

def agregar_titulo():
    global cantidad_libros  
    if cantidad_libros < 20:
        nuevo_titulo = input("Ingrese el título del nuevo libro: ")
        copias = int(input("Ingrese la cantidad de ejemplares: "))
        titulos[cantidad_libros] = nuevo_titulo
        ejemplares[cantidad_libros] = copias
        cantidad_libros += 1
    else:
        print("Capacidad máxima de libros alcanzada.")


def actualizar_ejemplares():
    print("Actualizar ejemplares")
    titulo = input("Título a actualizar: ")
    encontrado = False
    for i in range(cantidad_libros):
        if titulos[i] == titulo:
            print(f"Actualmente hay {ejemplares[i]} ejemplares de '{titulos[i]}'.")
            numero = int(input("Nueva cantidad de ejemplares: "))
            ejemplares[i] = numero
            print("Cantidad actualizada.")
            encontrado = True
    if not encontrado:
        print("Título no encontrado.")









