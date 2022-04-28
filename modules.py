from googlesearch import search

def busqueda(name):
  g_search = search(name, lang="ES", num_results=1)
  image = "https://www.google.com/" + g_search[1]
  print(g_search)
  print(image)
