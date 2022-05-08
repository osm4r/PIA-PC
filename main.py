import argparse
from argparse import RawTextHelpFormatter
import os

try: 
  import modules
  import virustotal
  import cifrado
  import portscan
except ImportError:
  os.system("pip install -r requirements.txt")
  print("Instalando librerias necesarias... Ejecute de nuevo")
  exit()

# Funcion principal
def main():
  # asd
  parser = argparse.ArgumentParser(description='Guia de uso de argumentos',
                                    formatter_class=RawTextHelpFormatter)

  # Se crean todos los argumentos funcionables del script
  parser.add_argument('-pS', '--portscan', required=False,
                      help='Dirección ip a escanear. Ej. python main.py -pS "[Direccion IP]"', action='store')

  parser.add_argument('-c', '--cifrar', required=False,
                      help='Cifrado de un texto. Ej. python main.py -E "[texto plano]"', action='store')

  parser.add_argument('-d', '--descifrar', required=False,
                      help='Descifrado de un texto. Ej. python main.py -D "[texto encriptado]"', action='store')
  
  parser.add_argument('-abc', '--alfabeto', type=str, help="Documento json con el alfabeto a utilizar con las llaves.")

  parser.add_argument("-i"  , "--image", type=str, help="Nombre a buscar en bing para descargar las imagenes")

  parser.add_argument("-cant"  , "--cantidad", type=int, help="Cantidad de imagenes a descargar. default = 5")

  parser.add_argument("-e1"  , "--email1", type=str, help="Correo destinatario a enviar metadatos")
  
  parser.add_argument("-pass"  , "--password", type=str, help="Contraseña de correo destinatario")

  parser.add_argument("-e2"  , "--email2", type=str, help="Correo remitente a enviar metadatos")

  parser.add_argument('-vt', '--virustotal', required=False, help='URL de pagina web a escanear con Virus Total')

  parser.add_argument('-key', '--apikey', required=False, help='api-key de la pagina virus total')

  # Se define la variable con los argumentos que podrían ser utilizados con argparse
  args = parser.parse_args()
  # print(args)

  # Se descargan imagenes y obtienen sus metadatos mediante el "artista" recibido por el parametro image
  if args.image:
    print("Busqueda:", args.image)

    if args.cantidad:
      modules.download_bing_image(args.image, args.cantidad)
    else:
      modules.download_bing_image(args.image, 5)
    
    dirs_images = modules.list_images(args.image)
    list = modules.get_metadata(dirs_images, args.image)

    # Se mandan los metadatos por correo (opcional) solo si se reciben los 3 parámetros: email1, password y email2
    if len(list) != 0 and args.email1 and args.password and args.email2:
      modules.send_email(list, args.image, args.email1, args.password, args.email2)

  # Se realiza un escaneo de puertos a la direccion ip recibida por medio del parametro portscan
  if args.portscan:
    portscan.ShootYourShot(args.portscan)

  # Se realiza el cifrado de una cadena que es recibida mediante el parametro cifrar
  if args.cifrar:
    if args.alfabeto:
      cifrado.cifrar(args.cifrar, args.alfabeto)
    else:
      print("El parametro '-abc' con archivo json es necesario")
      exit()

  # Se realiza el descifrado de una cadena que es recibida mediante el parametro descifrar
  if args.descifrar:
    if args.alfabeto:
      cifrado.descifrar(args.descifrar, args.alfabeto)
    else:
      print("El parametro '-abc' con archivo json es necesario")
      exit()

  # Se valida que haya cadena a cifrar o descifrar si se utiliza el parametro alfabeto
  if args.alfabeto:
    if not args.cifrar and not args.descifrar:
      print("El parametro '-c' con la cadena a cifrar es necesario")
      print("o")
      print("El parametro '-d' con la cadena cifrada es necesario")
      exit()   

  # Se valida que se reciban los parametros virustotal y apikey para realizar un escaneo de un URL en específico
  if args.virustotal:
    if not args.apikey:
      print("El parametro '-key' con el api-key de Virus Total es necesario")
      exit()

  # Se valida que se reciban los parametros virustotal y apikey para realizar un escaneo de un URL en específico
  if args.apikey:
    if args.virustotal:
      virustotal.scan_image(args.virustotal, args.apikey)
    else:
      print("El parametro '-vt' con el URL es necesario")
      exit()

  # Se obtienen los valores hash de todos los archivos del proyecto
  modules.get_hash(modules.list_folder())

# Metodo principal
if __name__ == '__main__':
  main()