import os
import shutil
import subprocess
import exifread
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bing_image_downloader import downloader

if not os.path.exists('logs'):
  os.makedirs('logs')
logging.basicConfig(filename="logs/reporte.log", filemode="a",
                    format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    level= logging.INFO)

# Funcion para descargar una imagen sobre algun tema/persona por medio de bing
def download_bing_image(name, cant):
  """
            Funcion para descargar una imagen sobre algun tema/persona por medio de bing.
            
            :Ejemplo:
    
            >>> download_bing_image('Messi', 15)        
            
            :param name: primer argumento
            :type name: string
            :param cant: segundo argumento
            :type cant: int
            """

  logging.info("Inicia busqueda de imagenes: "+ name)
  try:
    if cant > 99:
      print("Cantidad fuera del limite. Utilizando valor por default (5)")
      cant = 5

    # Si no existe la carpeta "data" se crea
    if not os.path.exists('data'):
      os.makedirs('data')
      logging.info("Se crea la carpeta data")
    else:
      logging.info("Ya existe la carpeta data")
    
    # Se descargan las imagenes del "artista" solicitado
    downloader.download(name, limit=cant,  output_dir=f"data/{name}", 
    adult_filter_off=True, force_replace=False, timeout=60)
    
    if os.path.exists(f"data/{name}/images"):
      shutil.rmtree(f"data/{name}/images")
      os.rename(f"data/{name}/{name}", f"data/{name}/images")
    else:
      os.rename(f"data/{name}/{name}", f"data/{name}/images")

    logging.info("Imagenes descargadas exitosamente")
  except Exception as e:
    logging.info("Ha ocurrido un error al tratar de descargar las imagenes")
    logging.error(e)

# Guarda las ubicaciones de las imagenes descargadas en una lista.
# Esta lista se utiliza para obtener los metadatos de las imagenes
def list_images(name):
  """
            Guarda las ubicaciones de las imagenes descargadas en una lista.
            Esta lista se utiliza para obtener los metadatos de las imagenes.
            
            :Ejemplo:
    
            >>> list_images('Messi')        
            
            :param name: primer argumento
            :type name: string
            """

  files_list = os.listdir(f"data/{name}/images")
  dirs = []
  for file in range(len(files_list)):
    dir = f"data/{name}/images/{files_list[file]}"
    dirs.append(dir)
  return dirs

# Funcion para obtener metadatos de las im??genes descargadas
def get_metadata(dirs, name):
  """
            Funcion para obtener metadatos de las im??genes descargadas.
            
            :Ejemplo:
    
            >>> get_metadata(["data\Messi\images\Image_1.jpg"], 'Messi')        
            
            :param dirs: primer argumento
            :type dirs: list
            :param name: segundo argumento
            :type name: string
            """

  # Si no existe la carpeta "metadata" se crea
  if not os.path.exists(f'data/{name}/metadata'):
    os.makedirs(f'data/{name}/metadata')
    logging.info("Se crea la carpeta metadata")
  else:
    logging.info("Ya existe la carpeta metadata")

  list_dir_image = []

  try:
    # Se obtienen los metadatos de cada imagen descargada y
    # se guardan en un archivo de texto por imagen
    for dir in range(len(dirs)):
      imagen = open(dirs[dir], 'rb')
      # Obtiene valores exif de imagen
      valores_exif = exifread.process_file(imagen)

      # Si la imagen no tiene metadatos no se crea el archivo
      if len(valores_exif) == 0:
        print(f"La imagen Image_{dir+1}.jpg no tiene metadatos")
        logging.warning(f"No se obtuvieron los metadatos de Image_{dir+1}.jpg")
        continue
      
      # Se crea el archivo de texto
      with open(f"data/{name}/metadata/Image_{dir+1}.txt", "a") as file:
        list_dir_image.append(f"data/{name}/metadata/Image_{dir+1}.txt")
        for tag in valores_exif.keys():
          file.write(str(tag) + " : " + str(valores_exif[tag]) + "\n")
          
      print("Se crea el archivo de metadatos "+ f"Image_{dir+1}.txt")
      logging.info("Se crea el archivo de metadatos "+ f"Image_{dir+1}.txt")
  except Exception as e:
    logging.error(e)

  if len(list_dir_image)==0:
    print("Ninguna imagen tiene metadatos")
    print("No se enviar?? el correo")
    logging.warning("Ninguna imagen tiene metadatos")
    logging.warning("No se enviar?? el correo")
  return list_dir_image

# Funcion para mandar correo con metadatos
def send_email(list_dir_image, name, email1, pswd, email2):
  """
            Funcion para mandar correo con metadatos.
            
            :Ejemplo:
    
            >>> send_email(["data\Messi\metadata\Image_1.txt"], 'Messi', 'patricia@gmail.com', 'contrase??a123', 'osmar@yahoo.com')        
            
            :param list_dir_image: primer argumento
            :type list_dir_image: list
            :param name: segundo argumento
            :type name: string
            :param email1: tercer argumento
            :type email1: string
            :param pswd: cuarto argumento
            :type pswd: string
            :param email2: quinto argumento
            :type email2: string
            """

  try:
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

    print("Se enviaron los archivos de metadatos al correo "+ email2)
    logging.info("Se enviaron los archivos de metadatos al correo "+ email2)
  except Exception as e:
    logging.warning(e)

# Guarda las ubicaciones de las carpetas/archivos a obtener su valor hash en una lista
def list_folder():
  """
            Guarda las ubicaciones de las carpetas/archivos a obtener su valor hash en una lista.
            
            :Ejemplo:
    
            >>> list_folder()        
            """

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

# Funcion para obtener el valor hash de todos los archivos del proyecto (MEDIANTE POWERSHELL)
def get_hash(list_folders):
  """
            Funcion para obtener el valor hash de todos los archivos del proyecto (MEDIANTE POWERSHELL).
            
            :Ejemplo:
    
            >>> get_hash(["escaneos", "data/Messi/images])        
            
            :param list_folders: primer argumento
            :type list_folders: list
            """

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
    logging.info("Documento de resultados hash_data.txt generado correctamente")
  except Exception as e:
    print(e)
    logging.error(e)
