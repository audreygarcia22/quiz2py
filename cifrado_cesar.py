

class cifrado_cesar :

    def __init__(self, desplazamiento):

        self.desplazamiento = desplazamiento

    def cifrar (self, clave):
        resultado = ""
        for letra in clave:
            
            if letra.isalpha():
                inicio = ord("A") if letra.isupper() else ord("a")
                
                siguiente_letra = chr((ord(letra) - inicio  + self.desplazamiento) % 26 + inicio )
               
                resultado += siguiente_letra
            else:
                resultado += letra  

        return resultado

# comentario


