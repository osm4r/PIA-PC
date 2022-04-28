from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs

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