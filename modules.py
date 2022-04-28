from googlesearch import search

def busqueda(name):
  g_search = search(name, num_results=3)
  print(g_search)
  for url in range(len(g_search)):
    print(f"url {url}", g_search[url])