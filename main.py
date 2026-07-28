import requests
import os
from dotenv import load_dotenv
from typing import Optional

# Carga las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")

# Realiza la petición a la API y convierte la respuesta a formato JSON
def obtener_datos_api() -> Optional[dict]:
    try:
        respuesta = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD", timeout=10)
        respuesta.raise_for_status() # si el status es 4xx o 5xx, lanza requests.exceptions.HTTPError aquí
        datos = respuesta.json()
        if datos['result'] == 'error':
            print("Error: la API reportó un problema, revisa tu clave o cuota")
            return
        return datos
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Revisa tu red")
    except requests.exceptions.Timeout:
        print("Error: El servidor tardo demasiado en responder")
    except requests.HTTPError:
        print("Error: la API respondió con un código de error HTTP")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Extrae los tasa de conversión
def extraer_tasa(datos_api: dict, codigo_seleccionado: str) -> float:
    tasa_conversion = datos_api["conversion_rates"][codigo_seleccionado]
    return round(tasa_conversion, 2)

# Orquesta el input y muestra el resultado final
def main() -> None:
    datos_api = obtener_datos_api()
    if datos_api is None: return
    # Bucle para solicitar al usuario el código de la moneda o que escriba 'salir' si desea terminar el programa
    while True:
        codigo_seleccionado = input("Escribe el codigo de tres letras de la moneda para buscar (por ejemplo: EUR, JPY o GBP) para conocer su equivalencia respecto al dólar estadounidense (o 'salir' para terminar): ").upper()
        if codigo_seleccionado.lower() == "salir":  
            print("Hasta luego")
            break
        try:
            resultado_final = extraer_tasa(datos_api, codigo_seleccionado)
            print(f"1 USD = {resultado_final} {codigo_seleccionado}")
        except KeyError:
            print("El código de moneda ingresado no existe.")

# Ejecuta solo si se esta en este archivo
if __name__ == "__main__":
    main()