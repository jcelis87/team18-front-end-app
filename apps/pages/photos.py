import datetime
import base64
import os
from urllib.parse import quote as urlquote
from dash_core_components.Dropdown import Dropdown
from flask import Flask, send_from_directory

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from apps.pages import progressbar, model_results

from app import app, server
from apps.utils.get_data import API_URL, send_file

import requests

CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-top": "1rem",
    "margin-right": "1rem",
    "padding-left": "1rem",
    "padding-bottom": "1rem",
    "width": "auto",
}

layout = html.Div(    
    [        
        dbc.Row(
            dbc.Col(html.H3("Nueva Imagen"), width=9, align="center"),justify="center"),
        dbc.Row(
            dbc.Col(
                dcc.Upload(
                    id="upload-image",
                    children=html.Div([
                        "Arrastre la imagen o ", 
                        html.A("Seleccione del disco duro")
                        ]),
                    style={
                        #"width": "60%",
                        #"height": "10%",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "10px",
                        "textAlign": "center",
                        #"margin": "10px"
                        #"align": "center"
                    },
                    # Allow multiple files to be uploaded
                    multiple=False
                ),
                width=9
            ),
            justify="center",
            className="h-50",
        ),
        dbc.Row(
            dbc.Col(html.Div("La imagen debe estar geo-referenciada y en formato GeoTiff."), width=9),
            justify="center"            
        ),
        dbc.Row(
            dbc.Col((html.Div(id="output-image-upload")))
        )
    ],
    id="model-content",
    style=CONTENT_STYLE,
)

def parse_contents(contents, filename):
    return html.Div([            
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload                                                
        dbc.Row(dbc.Col(html.H3("Analizar Imagen"), width=9), justify="center"),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id="model-selection",
                    options=[
                        {"label": "Model 1 (Split + Vision API)", "value": "model1"},
                        {"label": "Model 2 (EAST + pytesseract)", "value": "model2"},
                        {"label": "Model 3 (EAST + Vision API)", "value": "model3"}
                    ],
                    placeholder="Select a model...",
                    value="none",
                    style={
                        "width": "100%"
                    }
                ),
                width=6
            ),
            dbc.Col(
                html.Button("Run model", id="run-model"),
                width=3
            )
        ],
        justify="center"),
        dbc.Col(
            html.Img(
                src=contents,
                style={                    
                    "height": "auto",
                    "overflow": "hidden",
                    "object-fit": "cover",
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                    "width": "70%",
                    "padding": 10
                }
            )
        )            
    ])


@app.callback(Output("output-image-upload","children"),
              Input("upload-image","contents"),
              State("upload-image","filename"))
def update_output(contents, filename):
    if contents is None:
        raise dash.exceptions.PreventUpdate          
    path = requests.get(os.getenv("API_URL") + "/get_abspath").json()["path"]      
    imgstring = contents.split(",")[1]
    imgdata = base64.b64decode(imgstring)
    with open(os.path.join(path,"img_to_process.tif"), "wb") as f:
        f.write(imgdata)
        
    children = [
        parse_contents(contents, filename) 
    ]
    return children


@app.callback(Output("model-content","children"),              
              Input("run-model","n_clicks"),              
              State("model-selection","value"))
def run_model(n_clicks, model):
    
    # Get the id of the component that triggered the callback
    id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    print(id)
    print(model)

    if id == "run-model": 
        if model == "none":
            raise dash.exceptions.PreventUpdate
        
        if model == "model1":
            print(model)
            #requests.get(API_URL + "/process_img/")
            return progressbar.layout
