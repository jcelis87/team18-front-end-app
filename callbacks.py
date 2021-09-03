from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# main dash instance
from app import app

# call modules needed for callbacks
from apps.pages import map, photos, eda, map_overlay, model_results, progressbar, team18

# Entire callbacks definition
def register_callbacks(app):
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in ["/"]:
            return map.layout
        elif pathname == "/photos":
            return photos.layout
        elif pathname == "/eda":
            return eda.layout
        elif pathname == "/results":
            return map_overlay.layout
        elif pathname == "/team18":
            return team18.layout
        

        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )
