import os
import requests
import subprocess
import exifread
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
from bing_image_downloader import downloader

# Funcion para descargar una imagen sobre algun tema/persona por medio de bing
def download_bing_image(name):
  if not os.path.exists('data'):
    os.makedirs('data')
  downloader.download(name, limit=5,  output_dir=f"data/{name}", 
  adult_filter_off=True, force_replace=False, timeout=60)
  os.rename(f"data/{name}/{name}", f"data/{name}/images")

# Funcion para descargar imagen por url en específico
def download_image_by_url(url):
  response = requests.get(url)
  with open("imagen.jpg","wb")as file:
    for ima in response.iter_content(chunk_size=50000):
      file.write(ima)
    print("Se descargo correctamente la imagen")

def list_images(name):
  files_list = os.listdir(f"data/{name}/images")
  dirs = []
  for file in range(len(files_list)):
    dir = f"data/{name}/images/{files_list[file]}"
    dirs.append(dir)
  return dirs

# Funcion para obtener metadatos de las imágenes descargadas
def get_metadata(dirs, name):
  if not os.path.exists(f'data/{name}/metadata'):
    os.makedirs(f'data/{name}/metadata')

  list_dir_image = []
  for dir in range(len(dirs)):
    imagen = open(dirs[dir], 'rb')
    # Obtiene valores exif de imagen
    valores_exif = exifread.process_file(imagen)

    # Imprimir valores de la imagen
    print(len(valores_exif))
    if len(valores_exif) == 0:
      print(f"la imagen {dirs[dir]} no tiene metadatos")
      continue
    # print(valores_exif)
    
    with open(f"data/{name}/metadata/Image_{dir+1}.txt", "a") as file:
      list_dir_image.append(f"data/{name}/metadata/Image_{dir+1}.txt")
      for tag in valores_exif.keys():
        file.write(str(tag) + " : " + str(valores_exif[tag]) + "\n")

  return list_dir_image

# Funcion para mandar correo con metadatos
def send_email(list_dir_image):
  sender_email = "patricia.hernandezca@uanl.edu.mx"
  receiver_email = "osmarfishy@gmail.com"
  password = getpass.getpass()
  subject = "Metadata"
  text = "Metadata files"
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = subject
  message.attach(MIMEText(text, "plain"))
  
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

# Funcion para obtener el valor hash de uno o mas archivos o incluso una carpeta (MEDIANTE POWERSHELL)
def get_hash(*args):
  try:
    data = []
    for filepath in args:
      lineaPS = r"powershell -Executionpolicy Bypass -File .\getHash.ps1 -TargetFolder " + str(filepath)
      runningProcesses = subprocess.check_output(lineaPS)
      text = runningProcesses.decode().strip()
      text = text.replace("\r", "")
      data.append(text)

    with open("hash_data.txt", "w") as file:
      for hash in data:
        file.write(hash + "\n")

    print("Documento de resultados hash_data.txt generado correctamente")
  except Exception as e:
    print("Error: ", e)
