import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"

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
            dbc.Col(html.Img(src=IGAC_LOGO, height="50px")),
        ),
        # html.H2("Team 18", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Nueva Imagen", href="/photos", active="exact"),
                dbc.NavLink("Analisis", href="/dashboard", active="exact"),
                dbc.NavLink("Equipo 18", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="navbar-dark bg-primary",
    style=SIDEBAR_STYLE,
)


layout = html.Div([sidebar])
