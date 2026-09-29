# Análisis Macroeconómico de Argentina: Inflación vs. Tipo de Cambio

Un proyecto de ingeniería de datos y análisis financiero desarrollado en **Python** y **SQLite**, que automatiza la extracción de series temporales públicas, procesa uniones relacionales complejas y genera visualizaciones macroeconómicas avanzadas.

---

## 🚀 Descripción del Proyecto
Este proyecto tiene como objetivo estudiar la dinámica macroeconómica argentina reciente, relacionando la evolución de la tasa de inflación mensual oficial con el comportamiento del tipo de cambio oficial (cierre de mes). Implementa un flujo completo de **ETL (Extract, Transform, Load)**, almacenamiento local relacional y representación visual de doble escala.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.14+**
* **SQLite & DB Browser for SQLite:** Base de datos relacional ligera para el almacenamiento persistente.
* **Pandas:** Manipulación, limpieza y transformación de estructuras de datos (*DataFrames*).
* **Requests:** Consumo y conexión HTTP con APIs públicas de datos financieros.
* **Matplotlib:** Creación de gráficos profesionales de ejes duales (`twinx`).

---

## 📂 Estructura del Repositorio
```text
├── economia_arg.db            # Base de datos SQLite generada con las tablas maestras
├── etl_inflacion.py           # Script ETL para la descarga y carga del IPC histórico
├── etl_tipocambio.py          # Script ETL para la descarga y carga del tipo de cambio diario
├── analisis_cruzado.py        # Consulta SQL avanzada (JOIN y CTEs) para alinear frecuencias
└── grafico_final.py           # Script de visualización con ejes duales (Matplotlib)
```

---

## ⚙️ Pasos para Ejecutar el Proyecto

1. **Clona el repositorio o descarga los archivos en tu equipo:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Instala las dependencias necesarias:**
   ```bash
   pip install pandas requests matplotlib
   ```

3. **Ejecuta los scripts de extracción y carga (ETL):**
   * Para poblar la tabla de inflación:
     ```bash
     python etl_inflacion.py
     ```
   * Para poblar la tabla de tipo de cambio:
     ```bash
     python etl_tipocambio.py
     ```

4. **Genera el análisis cruzado y la visualización final:**
   ```bash
   python grafico_final.py
   ```

---

## 📊 Hallazgos y Visualización
El script final genera un gráfico de ejes duales que permite contrastar visualmente:
* **Eje Izquierdo (Línea Azul):** Evolución histórica del precio de venta del Dólar Oficial (ARS) al cierre de cada mes.
* **Eje Derecho (Barras Rojas):** Variación porcentual de la Inflación Mensual informada oficialmente.

*(Opcional: Añade aquí una captura de pantalla del gráfico final generado para que los reclutadores lo vean de un vistazo en GitHub)*

---

## 💡 Competencias Demostradas
* Ingesta automatizada de datos desde **APIs REST públicas**.
* Modelado y persistencia en **Bases de Datos Relacionales (SQLite)**.
* Escritura de consultas **SQL avanzadas** (Common Table Expressions - CTEs, funciones de agregación como `MAX()`, y uniones de series temporales de distinta frecuencia: diaria vs. mensual).
* Visualización de datos financieros de alto impacto con **Python**.