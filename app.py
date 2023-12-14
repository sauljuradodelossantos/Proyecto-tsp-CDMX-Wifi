# Importar las bibliotecas necesarias
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import os
import geopandas as gpd  # Agrega esta línea para importar Geopandas

# Obtener la ruta absoluta al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo CSV dentro de la carpeta 'assets'
archivo_csv = os.path.join(script_dir, 'assets', '2023-11-23-puntos_de_acceso_wifi.csv')

# Cargar los datos desde el nuevo archivo CSV
df = pd.read_csv(archivo_csv)  # Asegúrate de que el nombre del archivo sea correcto

# Filtrar para asegurar que todas las filas tengan coordenadas
df = df.dropna(subset=['latitud', 'longitud'])

# Asumiendo que existe una columna 'programa' en el DataFrame
programas = df['programa'].unique()

# Cargar los datos geoespaciales de las delegaciones
try:
    delegaciones = gpd.read_file('assets/delegaciones_cdmx.geojson')  # Asegúrate de tener un archivo GeoJSON con información de delegaciones
except FileNotFoundError:
    print("Error: Archivo 'delegaciones_cdmx.geojson' no encontrado. Asegúrate de que el nombre del archivo sea correcto.")
except Exception as e:
    print(f"Error al cargar el archivo GeoJSON 'delegaciones_cdmx.geojson': {e}")

# Iniciar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1("Mapa de Puntos de Acceso WiFi por Programa 2023", className='h1'),
    dcc.Dropdown(
        id='programa-selector',
        options=[{'label': i, 'value': i} for i in programas],
        value='Colonias_Periféricas',  # Valor por defecto
        className='dropdown-estilizado'
    ),
    dcc.Graph(id='mapa-calor', className='graph')
], className='body')

# Callback para actualizar el mapa de calor
@app.callback(
    Output('mapa-calor', 'figure'),
    [Input('programa-selector', 'value')]
)
def update_map(programa_seleccionado):
    filtered_df = df[df['programa'] == programa_seleccionado]
    fig = px.density_mapbox(filtered_df, lat='latitud', lon='longitud', 
                            radius=10, 
                            center={"lat": 19.36, "lon": -99.133209}, 
                            zoom=10, 
                            mapbox_style="carto-positron")  # Cambié el estilo a 'carto-positron'
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  # Reduje los márgenes para que se vea mejor
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
