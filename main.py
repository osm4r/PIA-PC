import argparse
from argparse import RawTextHelpFormatter
import modules
import virustotal
import Cifrado
from EscaneoDePuertos import EscaneosDePuertos


def main():
  '''print("-----------------------------------------")
  print(" Bienvenido al sistema de ciberseguridad\n"
        "")
  print("-----------------------------------------")'''

  parser = argparse.ArgumentParser(description='Guia de uso de argumentos',
                                    formatter_class=RawTextHelpFormatter)

  parser.add_argument('-pS', '--portscan', required=False,
                      help='Dirección ip a escanear. Ej. python main.py -pS "[Direccion IP]"', action='store')

  parser.add_argument('-E', '--encriptar', required=False,
                      help='Encriptar un texto. Ej. python main.py -E "[texto plano]"', action='store')

  parser.add_argument('-D', '--desencriptar', required=False,
                      help='Desencriptar un texto. Ej. python main.py -D "[texto encriptado]"', action='store')

  '''parser.add_argument('-k', '--keylogger', required=False,
                      help='Iniciar el Keylogger. Ej. python main.py -k\nPara finalizar presionar "ctrl + c"',
                      action='store_true')'''

  parser.add_argument("-i"  , "--image", type=str, help="Nombre a buscar en bing para descargar las imagenes")

  parser.add_argument("-url", dest="url", type=str, help="URL para descargar la imagen", required=False)

  parser.add_argument('-hv', '--hash', required=False, help='Ubicacion de archivo(s) o carpeta solicitar valores hash')

  parser.add_argument('-vt', '--virustotal', required=False, help='URL de pagina web a escanear con Virus Total')

  parser.add_argument('-key', '--apikey', required=False, help='api-key de la pagina virus total')


  args = parser.parse_args()
  # print(args)

  if args.image:
    print("Busqueda:", args.image)
    modules.download_bing_image(args.image)
    
    dirs_images = modules.list_images(args.image)
    list = modules.get_metadata(dirs_images, args.image)
    if len(list) == 0:
      print("No se encontraron metadatos en las imagenes")
      print("No se enviara el correo")

    else:
      modules.send_email(list, args.image)

  # modules.get_hash(r"C:\Users\larub\OneDrive\Escritorio\English\Session2.pdf") # Incluir 'r' antes de la cadena para que funcione

  if args.hash:
    modules.get_hash(args.hash)

  if args.portscan:
    EscaneosDePuertos.ShootYourShot(args.portscan)

  if args.encriptar:
    Cifrado.Encriptar(args.encriptar)

  if args.desencriptar:
    Cifrado.Desencriptar(args.desencriptar)

  if args.apikey:
    if args.virustotal:
      virustotal.scan_image(args.virustotal, args.apikey)
    else:
      print("El parametro '-vt' con el URL es necesario")
      exit()

  if args.virustotal:
    if args.apikey:
      virustotal.scan_image(args.virustotal, args.apikey)
    else:
      print("El parametro '-key' con el api-key de Virus Total es necesario")
      exit()

  modules.get_hash(modules.list_folder())
  '''if args.keylogger:
    KeyLogger.StartKeyLogger()'''

if __name__ == '__main__':
  main()