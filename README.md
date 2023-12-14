# Proyecto de Mapa de Puntos de Acceso WiFi por Programa en la CDMX

Este proyecto es una aplicación web creada con Dash y Plotly para visualizar un mapa de calor de Puntos de Acceso WiFi por Programa en la Ciudad de México.

## Configuración

Para comenzar, sigue estos pasos:

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local usando:

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para instalar las dependencias. Puedes crear uno usando:

```bash
python -m venv .venv
```

Activar el entorno virtual:

En Windows:
```bash
.venv\Scripts\activate
```

En MacOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```
pip install fiona
pip install shapely
pip install geopandas

### 4. Ejecutar la Aplicación

Para ejecutar la aplicación, usa:

```bash
python app.py
```

## Uso

Abre tu navegador y dirígete a `http://127.0.0.1:8050/` para ver la aplicación.

