import json
from pathlib import Path

def leer_datos_json(ruta_archivo):
    ruta = Path(ruta_archivo)
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    nombres = [item["nombre"] for item in datos]
    return nombres