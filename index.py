# Dash basic libraries
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import dash_auth
from dash.dependencies import Input, Output

# dash instance
from app import app, server

# callbacks import
from callbacks import register_callbacks

# Dash custom modules
from apps.main import main_header, main_sidebar, main_content, main_footer


USERNAMEINFO = [['igac','Team#18']]
auth = dash_auth.BasicAuth(app,USERNAMEINFO)

#main layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        main_header.layout,
        main_sidebar.layout,
        main_content.layout,
        #main_footer.layout
    ],
)

# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Col(
#                 #html.P("Header"),
#                 main_header.layout,
#                 width=12,
#                 style={"height": "100%", "background-color": "red"}
#             ),
#             className="h-auto",
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     #html.P("Sidebar"),
#                     main_sidebar.layout,
#                     width=3,
#                     style={"height": "100%", "background-color": "blue"}
#                 ),
#                 dbc.Col(
#                     main_content.layout,
#                     width=9,
#                     style={"height": "100%", "background-color": "cyan"}
#                 )            
#             ],
#             className="h-75",
#         ),
#         dbc.Row(
#             dbc.Col(
#                 main_footer.layout,
#                 width=12,
#                 style={"height": "100%", "background-color":"red"}
#             ),
#             className="h-auto"
#         ),
#     ],
#     style={"height": "100vh"}
# )

# Callbacks register
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
