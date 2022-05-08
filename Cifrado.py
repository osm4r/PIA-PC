import json

# Funcion para cifrar una cadena
def cifrar(frase, file):
    # Se obtiene el alfabeto del archivo json recibido
    with open(file, 'r') as file:
        abc = json.load(file)

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
def descifrar(frase, file):
    with open(file, 'r') as file:
        abc = json.load(file)

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
