from cifrado_cesar import cifrado_cesar

nombre = input("¿Cual es tu nombre? ")
print(f"Bienvenido {nombre}")

mensaje = int(input("Cántos espacios deseas moverte: ")) 

prueba = cifrado_cesar(mensaje)

cifrado = input("Ingrsa tu clave: ")
print(prueba.cifrar(cifrado))