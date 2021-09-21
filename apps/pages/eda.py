import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

colors = {"background": "#111111", "text": "#000000"}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-top": "3rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Data
sites = ["Sitio", "Quebrada", "Vereda", "Caserío", "Loma", "Cuchilla", "Cerro", "Laguna","Páramo",
         "Alto", "Filo", "Río", "Caño", "Mesa", "Nombre", "Cañón", "Corregimiento", "Serranía",
         "Aeropuerto", "Puente", "Meseta", "Inspección de Policía", "Cueva", "Central Eléctrica", "Zanjón"]         
count = [414,124,71,30,27,15,11,10,8,6,5,4,3,3,3,2,2,1,1,1,1,1,1,1,1,1]
df = pd.DataFrame(zip(sites,count), columns=["Tipo de sitio","Frecuencia"])

fig = px.bar(df, x="Tipo de sitio", y="Frecuencia", height=600)

fig.update_layout(
    font=dict(size=16)
)

layout = html.Div(
    id="",
    className="",
    children=[
        html.H3(
            children="Exploración Preliminar de Datos",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="La siguiente gráfica muestra los tipos de topónimos más comunes en Chaparral, Tolima, el cual fue el foco de nuestro proyecto.",
            style={"textAlign": "left", "color": colors["text"]},
        ),
        dcc.Graph(
            id="Graph1",
            figure=fig
        ),
    ],
    style=CONTENT_STYLE,
)