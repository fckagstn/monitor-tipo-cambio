# Monitor de Tipo de Cambio

CLI en Python que consulta tipos de cambio en tiempo real desde ExchangeRate-API y permite consultar de forma interactiva la equivalencia de distintas monedas respecto al dólar estadounidense (USD).

## ¿Por qué este proyecto?

Construí este proyecto porque me interesa trabajar con empresas del mercado **nearshore**, donde es común que las ofertas de empleo y los salarios se publiquen en dólares estadounidenses. Quería una herramienta sencilla que me permitiera consultar rápidamente el valor de una moneda respecto al USD, mientras practicaba el consumo de APIs REST, el manejo de variables de entorno y el tratamiento de errores en aplicaciones reales.

## Características

- Consulta tipos de cambio en tiempo real desde **ExchangeRate-API**.
- Soporta más de **160 monedas** utilizando su código ISO de tres letras.
- Permite realizar múltiples consultas sin reiniciar la aplicación.
- La entrada es insensible a mayúsculas y minúsculas (`mxn`, `MXN` o `Mxn` funcionan igual).
- Permite salir del programa escribiendo `salir`.
- Manejo de errores para:
  - Falta de conexión a Internet.
  - Tiempo de espera agotado (`timeout`).
  - Errores HTTP devueltos por la API.
  - Errores reportados por la propia API (como una API key inválida o cuota excedida).
  - Códigos de moneda inexistentes.
- Protección de la API key mediante variables de entorno utilizando un archivo `.env`.
- Código organizado en funciones con responsabilidades separadas para facilitar su mantenimiento.

## Requisitos

- Python 3.x
- Una API key gratuita de [ExchangeRate-API](https://www.exchangerate-api.com/)

## Instalación y uso

1. Clona este repositorio.

2. Crea y activa un entorno virtual.

```bash
python -m venv .venv
```

En Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

3. Instala las dependencias.

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz del proyecto con tu API key.

```env
EXCHANGE_API_KEY=tu_api_key_aqui
```

5. Ejecuta el programa.

```bash
python main.py
```

6. Escribe el código ISO de tres letras de la moneda que deseas consultar (por ejemplo: `MXN`, `EUR` o `JPY`).

7. Para finalizar el programa, escribe:

```text
salir
```

## Tecnologías

- **Python**
- **requests** — consumo de la API REST.
- **python-dotenv** — gestión de variables de entorno.
- **typing** — anotaciones de tipos (`Optional`, `dict`, `float` y `None`).
- **ExchangeRate-API** — obtención de tipos de cambio en tiempo real.

## Mejoras futuras

- Permitir convertir cualquier cantidad, no únicamente el valor de **1 USD**.
- Convertir entre dos monedas arbitrarias (por ejemplo, MXN → EUR).
- Mostrar el nombre completo de la moneda además del código ISO.
- Mostrar la fecha y hora de la última actualización proporcionada por la API.
- Empaquetar la aplicación como una herramienta instalable mediante `pip`.
