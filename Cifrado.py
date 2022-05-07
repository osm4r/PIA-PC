abc = {
        'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I',
        'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N',
        'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S',
        'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X',
        'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C',
        'Z': 'D', 
        'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i',
        'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n',
        'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's',
        'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x',
        'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c',
        'z': 'd'
    }

# Funcion para cifrar una cadena
def cifrar(frase):
    cadena_cifrada = ''
    for letra in frase:
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                cadena_cifrada += y
                encontrado = True
        if not encontrado:
            cadena_cifrada += letra
    print("Cadena encriptada: ", cadena_cifrada)

# Funcion para descifrar una cadena
def descifrar(frase):
    cadena_descifrada = ''
    for letra in frase:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                cadena_descifrada += x
                encontrado = True
        if not encontrado:
            cadena_descifrada += letra
    print("Cadena desencriptada: ", cadena_descifrada)
