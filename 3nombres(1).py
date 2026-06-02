nombres = []

for i in range(3):
 while True:
        nombre = input(f"Ingrese el nombre {i+1}: ")
        if len(nombre) >= 3:
         nombres.append(nombre)
         break
        else:
         print("debe tener mas de 3 letras el nombre")

longitud_maxima = max(len(nombre for nombre in nombres))

ganadores = [nombre for nombre in nombres if len(nombre) == longitud_maxima]

print(f"longitud maxima: {longitud_maxima}")

print("*"*40)
for i in ganadores:
   print(f"ganador: {nombre}")
print("*"*40)