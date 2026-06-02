nombres = []

for i in range(3):
 while True:
        nombre = input(f"Ingrese el nombre {i+1}: ")
        if len(nombre) >= 3:
         nombres.append(nombre)
         break
        else:
         print("debe tener mas de 3 letras el nombre")