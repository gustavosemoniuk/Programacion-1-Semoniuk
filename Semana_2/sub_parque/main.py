from parque import mostrar_atracciones
from parque import puede_subir
from parque import calcular_precio
from parque import registrar_visita
from parque import mostrar_resumen

print("Bienvenido a PythonLand")
nombre, edad = registrar_visita("", "")
print(f"Hola {nombre}, tenes {edad} años.")

atracciones = mostrar_atracciones() 

print(f"Has seleccionado las siguientes atracciones: {atracciones}")

# Verificar si puede subir a todas
puede_todas = True
for atr in atracciones:
    if not puede_subir(edad, atr):
        puede_todas = False
        break

if puede_todas:
    print("Puedes subir a todas las atracciones seleccionadas.")
else:
    print("No puedes subir a todas las atracciones seleccionadas.")

# Calcular precio total
precio_total = 0
for atr in atracciones:
    precio_total += calcular_precio(atr)

print("El precio será de:", precio_total)

print(mostrar_resumen(nombre, edad, atracciones))
