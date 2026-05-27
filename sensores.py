import requests
import random
import time
from datetime import datetime

URL = "http://127.0.0.1:8000/sensores"

print("Iniciando simulador de sensores...")

while True:

    datos = {
        "temperatura": round(random.uniform(15, 35), 2),
        "viento": round(random.uniform(0, 50), 2),
        "humedad": round(random.uniform(20, 90), 2),
        "aire": round(random.uniform(100, 500), 2)
    }

    try:
        response = requests.post(URL, json=datos)

        print("\n======================")
        print("Hora:", datetime.now().strftime("%H:%M:%S"))
        print("Datos enviados:", datos)
        print("Status:", response.status_code)
        print("Respuesta:", response.text)

    except Exception as e:
        print("Error enviando datos:", e)

    time.sleep(5)