import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

# Header
HEADER_STYLE = {
    "position": "sticky",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "3rem",
    "background-color": "#f8f9fa",
}

IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"


layout = html.Div(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=IGAC_LOGO, height="50px")),
                    dbc.Col(dbc.NavbarBrand("IGAC", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://www.igac.gov.co/",
        ),
    ],
    className="bg-primary",
    style=HEADER_STYLE,
)


# navbar = dbc.Navbar(
#     [
#         html.A(
#             # Use row and col to control vertical alignment of logo / brand
#             dbc.Row(
#                 [
#                     dbc.Col(html.Img(src=IGAC_LOGO, height="50px")),
#                     dbc.Col(dbc.NavbarBrand("IGAC", className="ml-2")),
#                 ],
#                 align="center",
#                 no_gutters=True,
#             ),
#             href="https://www.igac.gov.co/",
#         ),
#         dbc.NavbarToggler(id="navbar-toggler"),
#         # dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
#     ],
#     style=NAVBAR_STYLE,
# )
