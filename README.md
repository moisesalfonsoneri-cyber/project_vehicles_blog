# Vehicles US Market Explorer

## Descripcion
Aplicacion de analisis exploratorio de anuncios de autos usados en Estados Unidos, desarrollada con `pandas`, `plotly` y `streamlit` para visualizar patrones de precio y tiempo en inventario.

## Dataset usado
- Archivo: `vehicles_us.csv`
- Fuente interna del proyecto: listado histórico de vehículos usados.

## Visualizaciones incluidas
- Histograma de `days_listed` (distribución de días en inventario).
- Scatter plot de `price` vs `days_listed` (relación entre precio y tiempo publicado).

## Ejecucion local
1. Crear y activar entorno virtual.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la app:
   ```bash
   streamlit run app.py
   ```
4. Abrir en navegador la URL local mostrada por Streamlit (normalmente `http://localhost:8501`).

## Futuro despliegue en Render
El proyecto esta preparado para desplegarse como servicio web en Render usando Streamlit. El siguiente paso sera:
1. Conectar el repositorio en Render.
2. Configurar instalación con `pip install -r requirements.txt`.
3. Configurar inicio con `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`.
