MAX = 10

lista_alumnos = [""]*MAX
lista_libros = [0]*MAX
lista_comentarios = [""]*MAX

def cargar_datos():
    print("Carga de datos")

    for i in range(MAX):
        while True:
            nombre = input(f"Ingrese nombre del alumno {i+1} : ")
            if nombre != "":
                lista_alumnos [i] = nombre
                break
            else:
                print("Nombre no puede estar en blanco.")
        
        while True:
            libros = input("Cuantos libros ha leido (1-20): ")
                
            if libros != "":

                es_numero = True
                for c in libros:
                    if c < "0" or c > "9":
                            es_numero = False
                            break
                    
                if es_numero:
                    cantidad = int(libros)
                    if 1 <= cantidad <= 20:
                        lista_libros[i] = cantidad
                        break
                    else:
                        print("Ingrese un numero entre 1 y 20.")
                else:
                    print("Solo ingrese numeros.")
            else:
                print("Libros no puede estar vacio.")
        
        while True:
            comentario = input("Ingrese algun comentario sobre los libros leidos: ")
            if comentario != "":
                lista_comentarios [i] = comentario
                break
            else:
                print("Comentario no puede estar en blanco.")
        
        if i < 9:
            continuar = input("Quiere agregar otro alumno? (s/n): ").lower()
            if continuar == "n":
                break
        else:
            print("Se ha llegado al limite de alumnos.")
    

def mostrar_datos():
    print("Mostrar Datos")

    suma = 0
    cantidad = 0

    for i in range(MAX):
        if lista_alumnos[i] != "":
            print(f"{i+1}. Alumno: {lista_alumnos[i]}, Libros leidos: {lista_libros[i]}, Comentario: {lista_comentarios[i]}.")
            suma += lista_libros[i]
            cantidad += 1
    
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El promedio de libros leidos es de: {promedio}")
    else:
        print("No hay alumnos cargados.")


def ordenar_datos():
    print("Datos Ordenados")

    for i in range(MAX - 1):
        for j in range(MAX - 1 - i):
            if lista_libros[j] < lista_libros[j+1]:
                lista_libros[j], lista_libros[j+1] = lista_libros[j+1], lista_libros[j]
                lista_alumnos [j], lista_alumnos[j+1] = lista_alumnos[j+1], lista_alumnos[j]
                lista_comentarios[j], lista_comentarios[j+1] = lista_comentarios[j+1], lista_comentarios[j]

    for i in range(MAX):
        if lista_alumnos[i] != "":
            print(f"{i+1}. Alumno: {lista_alumnos[i]}, Libros leidos: {lista_libros[i]}, Comentario: {lista_comentarios[i]}.")


while True:
    print("---Menu Biblioteca---")
    print("1. Cargar Datos")
    print("2. Mostrar Datos Cargados")
    print("3. Ordenar Datos")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opcion (1-4): "))
    
    if opcion == 1:
        cargar_datos()
    elif opcion == 2:
        mostrar_datos()
    elif opcion == 3:
        ordenar_datos()
    elif opcion == 4:
        break
    else:
        print("Seleccione una Opcion Valida")