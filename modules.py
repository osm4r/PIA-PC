import os
import subprocess
import exifread
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bing_image_downloader import downloader
import logging

# Funcion para descargar una imagen sobre algun tema/persona por medio de bing
def download_bing_image(name, cant):

  #Se define el formato que tendra el logging
  if cant > 99:
    print("Cantidad exhorbitante. Utilizando valor por default (5)")
    cant = 5

  # Si no existe la carpeta "data" se crea
  if not os.path.exists('data'):
    os.makedirs('data')
    #logging.info("Se crea la carpeta data")
  #else:
    #logging.warning("Ya existe la carpeta data")
  
  # Se descargan las imagenes del "artista" solicitado
  downloader.download(name, limit=cant,  output_dir=f"data/{name}", 
  adult_filter_off=True, force_replace=False, timeout=60)
  os.rename(f"data/{name}/{name}", f"data/{name}/images")
  
  logging.basicConfig(filename=f"data/{name}"+"/reporte.log", filemode="w", format='%(asctime)s-%(process)d-%(levelname)s-%(message)s', level= logging.INFO)
  logging.info("Inicia busqueda de imagenes")
  logging.info("Imagenes descargadas")

# Guarda las ubicaciones de las imagenes descargadas en una lista.
# Esta lista se utiliza para obtener los metadatos de las imagenes
def list_images(name):
  files_list = os.listdir(f"data/{name}/images")
  dirs = []
  for file in range(len(files_list)):
    dir = f"data/{name}/images/{files_list[file]}"
    dirs.append(dir)
  return dirs

# Funcion para obtener metadatos de las imágenes descargadas
def get_metadata(dirs, name):
  # Si no existe la carpeta "metadata" se crea
  if not os.path.exists(f'data/{name}/metadata'):
    os.makedirs(f'data/{name}/metadata')
    logging.info("Se crea la carpeta metadata")
  else:
    logging.warning("Ya existe la carpeta metadata")

  list_dir_image = []

  # Se obtienen los metadatos de cada imagen descargada y
  # se guardan en un archivo de texto por imagen
  for dir in range(len(dirs)):
    imagen = open(dirs[dir], 'rb')
    # Obtiene valores exif de imagen
    valores_exif = exifread.process_file(imagen)
    logging.info("Se obtienen los metadatos de "+dirs[dir])

    # Si la imagen no tiene metadatos no se crea el archivo
    if len(valores_exif) == 0:
      print(f"la imagen {dirs[dir]} no tiene metadatos")
      logging.warning("No se obtuvieron los metadatos de "+ dirs[dir])
      continue
    
    # Se crea el archivo de texto
    with open(f"data/{name}/metadata/Image_{dir+1}.txt", "a") as file:
      list_dir_image.append(f"data/{name}/metadata/Image_{dir+1}.txt")
      logging.info("Se crea el archivo de metadatos "+ f"Image_{dir+1}.txt")
      for tag in valores_exif.keys():
        file.write(str(tag) + " : " + str(valores_exif[tag]) + "\n")

  return list_dir_image

# Funcion para mandar correo con metadatos
def send_email(list_dir_image, name, email1, pswd, email2):
  sender_email = email1
  receiver_email = email2
  password = pswd
  subject = name
  text = f"{name} metadata files"
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = subject
  message.attach(MIMEText(text, "plain"))
  
  # Se adjunta cada archivo a enviar
  for file in list_dir_image:
    archivo_adjunto = open(file, "rb")
    adjunto_MIME = MIMEBase ("application", "octet-stream")
    adjunto_MIME.set_payload(archivo_adjunto.read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header("Content-Disposition", "attachment; filename = {0}".format(os.path.basename(file)))
    message.attach(adjunto_MIME) 
  with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.ehlo
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    logging.info("Se enviaron los archivos de metadatos al correo "+ email1)

# Funcion para obtener el valor hash de todos los archivos del proyecto (MEDIANTE POWERSHELL)
def get_hash(list_folders):
  try:
    data = []
    # Se obtiene le valor hash de cada archivo
    for filepath in list_folders:
      lineaPS = r"powershell -Executionpolicy Bypass -File .\getHash.ps1 -TargetFolder " + str(filepath)
      runningProcesses = subprocess.check_output(lineaPS)
      text = runningProcesses.decode().strip()
      text = text.replace("\r", "")
      data.append(text)

    # Se guardan los valores hash en un documento de texto
    with open("hash_data.txt", "w") as file:
      for hash in data:
        file.write(hash + "\n")

    print("Documento de resultados hash_data.txt generado correctamente")
  except Exception as e:
    print("Error: ", e)

# Guarda las ubicaciones de las carpetas/archivos a obtener su valor hash en una lista
def list_folder():
  folders = []
  folders.append(os.getcwd())
  if os.path.exists(os.getcwd() + '/escaneos'):
    folders.append(os.getcwd() + '/escaneos')
  
  if os.path.exists(f'data'):
    data = os.listdir('data')
    for folder in data:
      artist = os.listdir('data/' + folder)
      for subfolder in artist:
        folders.append(os.getcwd() + '/data/' + folder + '/' + subfolder)

  return folders
