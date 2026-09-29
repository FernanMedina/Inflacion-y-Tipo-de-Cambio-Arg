import sqlite3
import pandas as pd

# 1. Conectarnos a nuestra base de datos SQLite
conexion = sqlite3.connect("economia_arg.db")

# 2. Consulta SQL cruzada (JOIN)
# Agrupamos el tipo de cambio por año-mes tomando el último valor ('venta') de cada período
# y lo cruzamos con la tabla de inflación por coincidencia de fecha mensual.
query = """
WITH tc_mensual AS (
    SELECT 
        substr(fecha, 1, 7) AS anio_mes,
        venta AS tc_oficial_fin_mes,
        fecha AS fecha_exacta_tc
    FROM tipo_cambio_oficial
    -- Filtramos para tomar el último registro disponible de cada mes
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
ORDER BY i.fecha DESC;
"""

# 3. Ejecutamos la consulta y la cargamos en un DataFrame
df_cruzado = pd.read_sql(query, conexion)
conexion.close()

# 4. Mostramos los últimos registros combinados
print("Primeros resultados del cruce SQL (Inflación vs Tipo de Cambio):")
print(df_cruzado.head(12))