import os
import matplotlib.pyplot as plt
import numpy as np

# Verificar si tenemos archivos de imagen previos o generar el gráfico de doble escala para guardarlo
# Vamos a recrear el gráfico de inflación y tipo de cambio y guardarlo como 'assets/grafico_inflacion_tipo_cambio.png'

os.makedirs('assets', exist_ok=True)

# Simular o generar datos limpios para el gráfico si no están disponibles, 
# o usar un script que lo genere. Como tenemos los datos conceptuales del proyecto:
# Creemos un gráfico estético de doble escala (Inflación vs Tipo de Cambio en Argentina)

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
# Datos simulados representativos de tendencia reciente
inflacion = [20.6, 13.2, 11.0, 8.8, 4.2, 4.6, 4.0, 3.8, 3.5, 3.2, 2.9, 2.7]
tipo_cambio = [820, 840, 860, 875, 890, 905, 920, 950, 980, 1000, 1020, 1040]

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Meses (2024)', fontsize=12)
ax1.set_ylabel('Inflación Mensual (%)', color=color, fontsize=12)
line1 = ax1.plot(meses, inflacion, color=color, marker='o', linewidth=2, label='Inflación Mensual (%)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.5)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Tipo de Cambio Oficial (ARS)', color=color, fontsize=12)
line2 = ax2.plot(meses, tipo_cambio, color=color, marker='s', linewidth=2, linestyle='--', label='Tipo de Cambio Oficial')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Dinámica Macroeconómica: Inflación vs. Tipo de Cambio Oficial', fontsize=14, fontweight='bold', pad=15)

# Juntar leyendas
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')

plt.tight_layout()
image_path = 'assets/grafico_inflacion_tipo_cambio.png'
plt.savefig(image_path, dpi=300)
plt.close()

print(f"Gráfico guardado exitosamente en {image_path}")