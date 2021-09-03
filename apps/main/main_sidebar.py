from apps.utils.get_data import API_URL
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

#IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"
#IGAC_LOGO = "https://drive.google.com/file/d/1mf_Dy1BfT_jspOLc6DQfD-E9kb9dAHYX/view?usp=sharing"
IGAC_LOGO = API_URL + "/image/logo"

# Sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.Div(
            dbc.Col(html.Img(src=IGAC_LOGO, height="100px")),
        ),
        # html.H2("Team 18", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Nueva Imagen", href="/photos", active="exact"),
                dbc.NavLink("Exploración de datos", href="/eda", active="exact"),
                dbc.NavLink("Resultados", href="/results", active="exact"),
                dbc.NavLink("Equipo 18", href="/team18", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="navbar-dark bg-primary",
    style=SIDEBAR_STYLE,
)


layout = html.Div([sidebar])
