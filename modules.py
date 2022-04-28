from googlesearch import search

def busqueda(name):
  g_search = search(name, num_results=1)
  if len(g_search) == 0:
    print("no results")
    exit()
  else:
    image = "https://www.google.com/" + g_search[1]
    # print(g_search)
    return image

def download_image():
  print()