import requests
import json
from datetime import datetime

# Coordenadas de Barcelona
LAT = 41.3888
LON = 2.159

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=temperature_2m"
)

response = requests.get(url)
data = response.json()

temps = data["hourly"]["temperature_2m"]

temp_max = max(temps)
temp_min = min(temps)
temp_avg = sum(temps) / len(temps)

result = {
    "temperatura_maxima": temp_max,
    "temperatura_minima": temp_min,
    "temperatura_media": round(temp_avg, 2)
}

today = datetime.now().strftime("%Y%m%d")
filename = f"temp_{today}.json"

with open(filename, "w") as file:
    json.dump(result, file, indent=4)

print(f"Archivo {filename} creado correctamente")
