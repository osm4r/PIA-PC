from googlesearch import search

def busqueda(name):
  g_search = search(name, num_results=1)
  image = "https://www.google.com/" + g_search[2]
  print(g_search)
  print(image)
