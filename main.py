import argparse
from argparse import RawTextHelpFormatter
import modules
import Cifrado
# import KeyLogger
from WebScrapping import WebScrappingProgram
from EscaneoDePuertos import EscaneosDePuertos


def main():
  '''print("-----------------------------------------")
  print(" Bienvenido al sistema de ciberseguridad\n"
        "")
  print("-----------------------------------------")'''

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

  '''parser.add_argument('-k', '--keylogger', required=False,
                      help='Iniciar el Keylogger. Ej. python main.py -k\nPara finalizar presionar "ctrl + c"',
                      action='store_true')'''

  parser.add_argument("-i"  , "--image", type=str, help="Nombre a buscar en bing para descargar las imagenes", default="Messi")
  parser.add_argument("-url", dest="url", type=str, help="URL para descargar la imagen", required=False)
  parser.add_argument('-hv', '--hash', required=False, help='Ubicacion de archivo(s) o carpeta solicitar valores hash')
  # URL MESSI http://c.files.bbci.co.uk/14554/production/_114248238_messi-pa.jpg

  args = parser.parse_args()
  print(args)

  print("Busqueda:", args.image)
  modules.download_bing_image(args.image)
  if args.url is not None:
    modules.download_image_by_url(args.url)
  
  dirs_images = modules.list_images(args.image)
  list = modules.get_metadata(dirs_images, args.image)
  if len(list) == 0:
    print("No se encontraron metadatos en las imagenes")
  else:
    modules.send_email(list, args.image)

  # modules.get_hash(r"C:\Users\larub\OneDrive\Escritorio\English\Session2.pdf") # Incluir 'r' antes de la cadena para que funcione

  if args.hash:
    modules.get_hash(args.hash)
  
  if args.webscrapping:
    WebScrappingProgram.mainWS(args.webscrapping)

  if args.portscan:
    EscaneosDePuertos.ShootYourShot(args.portscan)

  if args.encriptar:
    Cifrado.Encriptar(args.encriptar)

  if args.desencriptar:
    Cifrado.Desencriptar(args.desencriptar)

  '''if args.keylogger:
    KeyLogger.StartKeyLogger()'''


if __name__ == '__main__':
  main()