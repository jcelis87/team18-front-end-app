import dash
import dash_bootstrap_components as dbc

external_scripts = [
    {"src": "https://kit.fontawesome.com/44d65a8b68.js"},
    {"crossorigin": "anonymous"},
]

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    title="Team 18",
    external_scripts=external_scripts,
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    ],
)

server = app.server
app.config.suppress_callback_exceptions = True
