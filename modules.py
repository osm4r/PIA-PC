from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs
import subprocess

def busqueda(name):
  g_search = search(name, num_results=1)
  if len(g_search) == 0:
    print("no results")
    exit()
  else:
    image = "https://www.google.com/" + g_search[1]
    # print(g_search)
    # print(image)
    return image

def download_image(url):
  response = requests.get(url)

  soup = bs(response.content, "html.parser")
  # po es una lista con todas las coincidencias de la etiqueta <img>
  po = soup.find_all('img')
  print(po)
  '''with open("imagen.jpg","wb")as file:
    for ima in response.iter_content(chunk_size=50000):
        file.write(ima)
    print("Se descargo correctamente la imagen")'''

# Funcion para obtener el valor hash de uno o mas archivos o incluso una carpeta (MEDIANTE POWERSHELL)
# Osmar Abelardo Bustos Vazquez
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
