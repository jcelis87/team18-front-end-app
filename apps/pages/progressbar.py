import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import dash
from app import app
from apps.pages import model_results
from dash.dependencies import Input, Output
from apps.utils.get_data import API_URL
import requests

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    html.H5("Procesando imagen..."),                    
                    style={
                        "height": "6rem",
                        "color": "black",
                        "text-align": "center"
                    }
                ),
                width=12
            ),
            justify="center"
        ),           
                
        dbc.Row(
            dbc.Col(
                dcc.Interval(id="progress-interval", n_intervals=0, interval=100, max_intervals=150),            
                width=12
            ),
            justify="center"
        ),
        dbc.Row(
            dbc.Col(
                dbc.Progress(id="progress"), width={"size":6}
            ),
            justify="center"
        )        
        
    ],
    id="bar-content"
)


@app.callback(
    [Output("progress", "value"), Output("progress", "children")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    #print(n)
    if n == 0:
        requests.get(API_URL + "/process_img/")
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much    
    return progress, f"{progress} %" if progress >= 5 else ""


@app.callback(Output("bar-content", "children"),
              Input("progress","value"))
def show_results(prog_value):
    if prog_value < 100:
        raise dash.exceptions.PreventUpdate               
    return model_results.layout