import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Conectarnos a la base de datos y extraer los datos cruzados
conexion = sqlite3.connect("economia_arg.db")

query = """
WITH tc_mensual AS (
    SELECT 
        substr(fecha, 1, 7) AS anio_mes,
        venta AS tc_oficial_fin_mes,
        fecha AS fecha_exacta_tc
    FROM tipo_cambio_oficial
    WHERE fecha IN (
        SELECT MAX(fecha) 
        FROM tipo_cambio_oficial 
        GROUP BY substr(fecha, 1, 7)
    )
)
SELECT 
    i.fecha AS fecha_inflacion,
    i.valor AS inflacion_mensual_pct,
    t.tc_oficial_fin_mes
FROM inflacion i
JOIN tc_mensual t ON i.fecha = t.fecha_exacta_tc
-- Filtramos por ejemplo los últimos 5 años para que el gráfico sea bien legible
WHERE i.fecha >= '2021-01-01'
ORDER BY i.fecha ASC;
"""

df = pd.read_sql(query, conexion)
conexion.close()

# Convertir la columna de fecha a formato datetime para una mejor lectura en el gráfico
df['fecha_inflacion'] = pd.to_datetime(df['fecha_inflacion'])

# 2. Configuración de la figura con Matplotlib (Ejes duales)
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfico 1: Tipo de Cambio Oficial (Línea Azul en el Eje Principal - izq)
color = 'tab:blue'
ax1.set_xlabel('Fecha (Cierre de Mes)', fontsize=10, fontweight='bold')
ax1.set_ylabel('Dólar Oficial (ARS)', color=color, fontsize=10, fontweight='bold')
linea1 = ax1.plot(
    df['fecha_inflacion'],
    df['tc_oficial_fin_mes'],
    color=color,
    linewidth=2.5,
    label='Dólar Oficial (Fin de Mes)',
)
ax1.tick_params(axis='y', labelcolor=color)

# Creamos un segundo eje que comparta el mismo eje X (twinx)
ax2 = ax1.twinx()

# Gráfico 2: Inflación Mensual (Barras rojas semitransparentes en el Eje Secundario - der)
color = 'tab:red'
ax2.set_ylabel('Inflación Mensual (%)', color=color, fontsize=10, fontweight='bold')
barras = ax2.bar(df['fecha_inflacion'], df['inflacion_mensual_pct'], color=color, alpha=0.4, width=20, label='Inflación Mensual (%)')
ax2.tick_params(axis='y', labelcolor=color)

# Título y diseño general
plt.title('Evolución Histórica: Dólar Oficial vs. Inflación Mensual en Argentina', fontsize=12, fontweight='bold', pad=15)
ax1.grid(True, linestyle='--', alpha=0.5)

# Mostrar la visualización
fig.tight_layout()
plt.show()