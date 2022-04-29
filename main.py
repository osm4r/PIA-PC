import argparse
import modules

parser = argparse.ArgumentParser()
parser.add_argument("-T", dest="thing", type=str, help="Nombre a buscar en bing para descargar las imagenes", default="Messi")
parser.add_argument("-url", dest="url", type=str, help="URL para descargar la imagen", required=False)
# URL MESSI http://c.files.bbci.co.uk/14554/production/_114248238_messi-pa.jpg

params = parser.parse_args()

def main():
  print("Busqueda:", params.thing)
  modules.download_bing_image(params.thing)
  if params.url is not None:
    modules.download_image_by_url(params.url)

  # modules.get_hash("C:\\Users\\osm4r\\Desktop\\piaa", "C:\\Users\\osm4r\\Desktop\\Sway.pdf") # "C:\\Users\\osm4r\\Desktop\\Sway.pdf"

if __name__ == '__main__':
  main()