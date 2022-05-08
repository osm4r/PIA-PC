import json

# Funcion para obtener el alfabeto para cifrar mediante un archivo json
def get_abc():
    with open('alfabeto.json', 'r') as file:
        abc = json.load(file)
    return abc

# Funcion para cifrar una cadena
def cifrar(frase):
    abc = get_abc()
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
    abc = get_abc()
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
