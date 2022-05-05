import Cifrado
import KeyLogger
from WebScrapping import WebScrappingProgram
from EscaneoDePuertos import EscaneosDePuertos
from argparse import RawTextHelpFormatter
import argparse
import subprocess
import sys




def main():
    print("-----------------------------------------")
    print(" Bienvenido al sistema de ciberseguridad\n"
          "")
    print("-----------------------------------------")

    parser = argparse.ArgumentParser(description='Guia de uso de argumentos',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('-wS', '--webscrapping', required=False,
                        help='Nombre de persona a investigar, Ej. python main.py -wS "[Nombre]"', action='store')

    parser.add_argument('-pS', '--portscan', required=False,
                        help='Dirección ip a escanear. Ej. python main.py -pS "[Direccion IP]"', action='store')

    parser.add_argument('-E', '--encriptar', required=False,
                        help='Encriptar un texto. Ej. python main.py -E "[texto plano]"', action='store')

    parser.add_argument('-D', '--desencriptar', required=False,
                        help='Desencriptar un texto. Ej. python main.py -D "[texto encriptado]"', action='store')

    parser.add_argument('-k', '--keylogger', required=False,
                        help='Iniciar el Keylogger. Ej. python main.py -k\nPara finalizar presionar "ctrl + c"',
                        action='store_true')

    args = parser.parse_args()

    if args.webscrapping:
        WebScrappingProgram.mainWS(args.webscrapping)

    if args.portscan:
        EscaneosDePuertos.ShootYourShot(args.portscan)

    if args.encriptar:
        Cifrado.Encriptar(args.encriptar)

    if args.desencriptar:
        Cifrado.Desencriptar(args.desencriptar)

    if args.keylogger:
        KeyLogger.StartKeyLogger()

# exit_code = subprocess.call([sys.executable, './ligagithub.sh'])


if __name__ == "__main__":
    main()
#
#
# #print("-----------------------------------------\n"
#  #     "          Hacking Tool for PC \n"
#   #    "-----------------------------------------")
#
# #Menu
# print("(1) Web Scrapping\n"
#      "(2) Escaneo de puertos\n"
#      "(3) Cifrado de mensajes\n"
#      "(4) Envío de correos\n"
#      "(5) Keylogger\n"
#      "(6) Salir\n")
#
# patron = re.compile(r'[1-6]')
#
# opcion = input("Opcion: ")
#
# #ArgParse
# # parser = argparse.ArgumentParser(description='Hacking Tool')
# # parser.add_argument('-wS',metavar='nombre', type=str, help='   Persona a buscar')
# # args = parser.parse_args()
# # nombre = args.wS
# # WebScrappingProgram.mainWS(nombre)
#
#
#
#
# while True:
#       if patron.match(opcion):
#             # WebScrapping
#             if opcion == '1':
#                 nombre = input("Ingresar el nombre de persona a extraer información")
#                 WebScrappingProgram.mainWS(nombre)
#
#
#             #Escaneo de puertos
#             elif opcion == '2':
#                   EscaneosDePuertos.ShootYourShot()
#                   break
#
#             #Cifrado de mensajes
#             elif opcion == '3':
#                   Cifrado.StartTheGame()
#                   break
#             #Envio de correos
#             elif opcion == '4':
#                   EnvioDeCorreos.EDC()
#                   break
#
#             #KeyLogger
#             elif opcion == '5':
#                   KeyLogger.StartKeyLogger()
#                   break
#
#             #Salir
#             elif opcion == '6':
#                 exit()
#
#             break
#       else:
#             opcion = input("Escribir una opción valida: ")
#
#
#
# import hashlib
#
# def encrypt_string(hash_string) :
#
# sha_signature = \
#
# hashlib.sha256(hash_string.encode()).hexdigest()
#
# return sha_signature
#
# hash_string = 'confidential data'
#
# sha_signature = encrypt_string(hash_string)
#
# print (sha_signature)
#
#
#
# #http://docs.python.org/3/library/hashlib.html
#
# import hashlib
#
# import os
#
#
#
# path = input ("se escribe el nombre del archivo ")
#
#
#
# file_obj = open (path, "rb")
#
# file = file_obj.read()
#
#
#
# Hash = hashlib.sha512(file)
#
# print (Hash)


