import sqlite3
import pandas as pd
import requests

# 1. Endpoint para el tipo de cambio (ej: Dólar Oficial / Mayorista o MEP)
# Usaremos el histórico del dólar oficial como base principal
url_tc = "https://api.argentinadatos.com/v1/cotizaciones/dolares/oficial"

print("Descargando datos históricos del tipo de cambio desde la API...")

try:
  # 2. Petición HTTP GET
  response = requests.get(url_tc)
  response.raise_for_status()
  data = response.json()

  # 3. Transformación a DataFrame de Pandas
  df_tc = pd.DataFrame(data)

  print("\nPrimeros registros obtenidos:")
  print(df_tc.head())

  # 4. Conexión a SQLite y volcado de datos en una nueva tabla
  conexion = sqlite3.connect("economia_arg.db")
  df_tc.to_sql("tipo_cambio_oficial", conexion, if_exists="replace", index=False)
  conexion.close()

  print(
      "\n¡Proceso completado! La tabla 'tipo_cambio_oficial' se guardó en"
      " 'economia_arg.db'."
  )

except requests.exceptions.RequestException as e:
  print(f"Error de conexión con la API: {e}")
except Exception as e:
  print(f"Ocurrió un error inesperado: {e}")