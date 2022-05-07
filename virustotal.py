import os
import base64
import json
import requests

# Funcion para escanear una URL en específico
def scan_image(link, key):
    id = base64.urlsafe_b64encode(link.encode()).decode().strip("=")
    url = f"https://www.virustotal.com/api/v3/urls/{id}"

    headers = {
    "Accept": "application/json",
    "x-apikey": f"{key}"
    }

    response = requests.request("GET", url, headers=headers)

    # Manda un error si la api-key no es valida
    if response.status_code == 401:
        print("\nInserte una API-KEY válida")
        exit()

    # Manda un error si la pagina web no es valida
    if response.status_code == 404:
        print("Error al tratar de analizar la página: ", link)
        exit()

    inf_resp = json.loads(response.text)
    print("Análisis correcto de: ", link.strip())

    # Si no existe la carpeta "escaneos" se crea
    if not os.path.exists('escaneos'):
        os.makedirs('escaneos')

    try:
        for num in range(0, 999):
            if os.path.exists(f'escaneos/escaneo_{num}.txt'):
                continue
            else:
                with open(f'escaneos/escaneo_{num}.txt', 'w') as file:
                    json.dump(inf_resp, file)
                print(f"Archivo escaneo_{num}.txt generado correctamente")
                break
    except Exception as e:
        print(e)
