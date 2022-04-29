import argparse
import modules

parser = argparse.ArgumentParser()
parser.add_argument("-T", dest="thing", type=str, help="Cosa xd", default="Messi")
params = parser.parse_args()

def main():
  print(params.thing)
  image_url = modules.busqueda(params.thing)
  modules.download_image(image_url)
  modules.get_hash("C:\\Users\\osm4r\\Desktop\\piaa", "C:\\Users\\osm4r\\Desktop\\Sway.pdf") # "C:\\Users\\osm4r\\Desktop\\Sway.pdf"

if __name__ == '__main__':
  main()