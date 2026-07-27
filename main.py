import requests
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")

# Realiza la petición a la API y convierte la respuesta a formato JSON
try:
    respuesta = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD", timeout=10)
    datos_api = respuesta.json()

    # Solicita al usuario el código de la moneda
    print("Escribe el código de tres letras de la moneda (por ejemplo: EUR, JPY o GBP) para conocer su equivalencia respecto al dólar estadounidense (USD).")
    codigo_seleccionado = input("Escribe el código de la moneda: ").upper()

    try:
        tasa_conversion = datos_api["conversion_rates"][codigo_seleccionado]
        tasa_redondeada = round(tasa_conversion, 2)
        print(f"1 USD = {tasa_redondeada} {codigo_seleccionado}")
    except KeyError:
        print("El código de moneda ingresado no existe.")

except requests.exceptions.ConnectionError:
    print("Error: No se pudo conectar al servidor. Revisa tu red")
except requests.exceptions.Timeout:
    print("Error: El servidor tardo demasiado en responder")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
