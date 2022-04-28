import argparse
import modules

parser = argparse.ArgumentParser()
parser.add_argument("-T", dest="thing", type =str, help="Cosa xd", default = "Messi")
params = parser.parse_args()

def main():
  print(params.thing)
  modules.busqueda(params.thing)
  

if __name__ == '__main__':
  main()