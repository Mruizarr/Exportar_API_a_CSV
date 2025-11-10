import requests
import csv
import json
import os
from typing import List, Dict, Any

# --- Configuración ---
# Puedes usar variables de entorno para una mejor seguridad
# API_KEY = os.environ.get("YOUR_API_KEY") 

# Ejemplo de datos de configuración (AJUSTA ESTO a tu API real)
API_URL = "https://api.example.com/v1/data"  # Cambia por la URL de tu API
API_KEY = "tu_clave_secreta_aqui"           # CAMBIA ESTO por tu clave real
OUTPUT_FILENAME = "datos_extraidos.csv"
DATA_KEY = "results" # Clave del diccionario JSON que contiene la lista de registros (e.g., response['results'])

def fetch_data_from_api(url: str, api_key: str) -> List[Dict[str, Any]]:
    """
    Realiza la llamada autenticada a la API y devuelve los datos parseados.
    """
    print(f"🔗 Llamando a la API: {url}...")
    
    # Cabeceras para la autenticación (ejemplo común)
    headers = {
        "Authorization": f"Bearer {api_key}", # O "X-API-Key": api_key, según la API
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Lanza una excepción para códigos de error HTTP

        data = response.json()
        
        # Verifica y extrae la lista de registros de la respuesta JSON
        if DATA_KEY in data and isinstance(data[DATA_KEY], list):
            print(f"✅ Datos obtenidos. Se encontraron {len(data[DATA_KEY])} registros.")
            return data[DATA_KEY]
        elif isinstance(data, list):
             print(f"✅ Datos obtenidos. Se encontraron {len(data)} registros (la respuesta es una lista directa).")
             return data
        else:
            print(f"❌ Error: La respuesta JSON no contiene la clave de datos esperada ('{DATA_KEY}') o no es una lista.")
            # Si el script se ejecuta contra una API real, aquí deberías inspeccionar la estructura de `data`
            # print("Respuesta completa de la API (solo primeras 500 chars para depuración):")
            # print(json.dumps(data, indent=2)[:500])
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al realizar la llamada API: {e}")
        return []

def save_to_csv(data: List[Dict[str, Any]], filename: str):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """
    if not data:
        print("⚠️ No hay datos para guardar en CSV.")
        return

    # Obtiene las cabeceras (nombres de las columnas) del primer registro
    fieldnames = list(data[0].keys())

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
            
        print(f"💾 Datos guardados exitosamente en: **{filename}**")
    except Exception as e:
        print(f"❌ Error al guardar en CSV: {e}")

def main():
    """
    Función principal para orquestar la extracción y guardado de datos.
    """
    if not API_KEY or API_KEY == "tu_clave_secreta_aqui":
        print("🚨 Por favor, actualiza la variable API_KEY con tu clave de autenticación real.")
        return

    # 1. Llamada a la API y parseo de JSON
    records = fetch_data_from_api(API_URL, API_KEY)
    
    # 2. Guardado automático en CSV
    save_to_csv(records, OUTPUT_FILENAME)

if __name__ == "__main__":
    main()

# --- Notas adicionales para el usuario ---
# Para usar este script, necesitarás instalar: pip install requests
# Si la API que usas tiene una paginación (más de 100/1000 registros), 
# necesitarás añadir un bucle en 'fetch_data_from_api' para llamar a todas las páginas.