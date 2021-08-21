import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "4rem 2rem 1rem",
    "background-color": "#f8f9fa",
    "z-index": "-1",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    #"width":"16rem",
    "margin-left": "18rem",
    "margin-right": "2rem",
    #"padding": "2rem 1rem",
}

layout = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Nueva Imagen", href="/page-1", active="exact"),
                dbc.NavLink("Analisis", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

<<<<<<< HEAD
# content = html.Div(style=CONTENT_STYLE)

# html.Div([sidebar])
=======

IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=IGAC_LOGO, height="100px")),
                    dbc.Col(dbc.NavbarBrand("IGAC", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://www.igac.gov.co/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        #dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)



content = html.Div(style=CONTENT_STYLE)


layout = html.Div([navbar, sidebar, content])
>>>>>>> ab252f155652a6a328b974b617667227f6979b6d
