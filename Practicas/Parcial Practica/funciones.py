def cargar_datos(nomb, punt, comm):
    print("Menu Cargar Datos")
    
    for i in range(10):
        while True:
            nombre = input(str("Ingrese nombre del participante: "))
            if nombre != "":
                nomb[i] = nombre
                break
            else:
                print("Nombre no puede estar vacio")
        
        while True:
            opinion = input("Ingrese su opinión (1-10): ")
            if opinion == "1" or opinion == "2" or opinion == "3" or opinion == "4" or opinion == "5" or opinion == "6" or opinion == "7" or opinion == "8" or opinion == "9" or opinion == "10":
                punt[i] = int(opinion)
                break
            else:
                print("Puntuación inválida. Debe ser un número entre 1 y 10.")
        
        while True:
            comentario = input("Comentario a dejar: ")
            if comentario != "":
                comm[i] = comentario
                break
            else:
                print("El comentario no puede estar en blanco.")
        if i < 9:
            seguir = input("Quiere agregar otro participante? s/n: ").lower()
            if seguir != "s":
                break
        else:
            print("se ha llegado al maximo de participantes")
        
        

def mostrar_datos(nomb, punt, comm):
    print("Datos Cargados")
    suma = 0       
    cantidad = 0
    
    for i in range(10):
        if nomb[i] != "":
            print(f"Nombre del participante {i+1}, {nomb[i]}, Puntuacion {punt[i]} y comentario {comm[i]}")
            suma += punt[i]
            cantidad +=1
    
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El promedio de puntuacion es de: {promedio}")
    else:
        print("No hay participantes cargados.")
    
    
    

def ordenar_datos(nomb, punt, comm):
    print("Datos Ordenados por mayor puntuacion")
    cantidad = 10
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if punt[j] < punt[j+1]:
                punt[j], punt[j+1] = punt[j+1], punt[j]
                nomb[j], nomb[j+1] = nomb[j+1], nomb[j]
                comm[j], comm[j+1] = comm[j+1], comm[j]
    
    for i in range(cantidad):
        if nomb[i] != "":
            print(f"{i+1}. {nomb[i]} - Puntaje: {punt[i]} - Comentario: {comm[i]}")
