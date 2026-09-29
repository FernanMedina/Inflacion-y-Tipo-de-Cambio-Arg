import sqlite3
import pandas as pd
import requests

# 1. Endpoint oficial de inflación de ArgentinaDatos
url_inflacion = "https://api.argentinadatos.com/v1/finanzas/indices/inflacion"

print("Descargando datos históricos de inflación desde la API...")

try:
  # 2. Petición HTTP GET
  response = requests.get(url_inflacion)
  response.raise_for_status()  # Verifica que la respuesta sea exitosa (código 200)
  data = response.json()

  # 3. Transformación a DataFrame de Pandas
  df_inflacion = pd.DataFrame(data)

  print("\nPrimeros registros obtenidos:")
  print(df_inflacion.head())

  # 4. Conexión a SQLite y volcado de datos
  # Esto creará (o actualizará) el archivo 'economia_arg.db' y la tabla 'inflacion'
  conexion = sqlite3.connect("economia_arg.db")
  df_inflacion.to_sql("inflacion", conexion, if_exists="replace", index=False)
  conexion.close()

  print(
      "\n¡Proceso completado! La tabla 'inflacion' se guardó en"
      " 'economia_arg.db'."
  )

except requests.exceptions.RequestException as e:
  print(f"Error de conexión con la API: {e}")
except Exception as e:
  print(f"Ocurrió un error inesperado: {e}")