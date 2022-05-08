import json
import os
import logging

if not os.path.exists('logs'):
  os.makedirs('logs')
logging.basicConfig(filename="logs/reporte.log", filemode="a",
                    format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    level= logging.INFO)

# Funcion para cifrar una cadena
def cifrar(frase, file):
    try:
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
        print("Cadena cifrada: ", cadena_cifrada)
        logging.info("Cadena descifrada: " + frase)
        logging.info("Cadena cifrada: " + cadena_cifrada)
    except Exception as e:
        logging.error(e)

# Funcion para descifrar una cadena
def descifrar(frase, file):
    try:
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
        print("Cadena descifrada: ", cadena_descifrada)
        logging.info("Cadena cifrada: " + frase)
        logging.info("Cadena descifrada: " + cadena_descifrada)
    except Exception as e:
        logging.error(e)
