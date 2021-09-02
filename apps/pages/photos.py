import datetime
import base64
import os
from urllib.parse import quote as urlquote
from flask import Flask, send_from_directory

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from apps.utils.get_data import send_file

import requests

CONTENT_STYLE = {
    "margin-left": "16rem",
    #"margin-top": "1rem",
    "margin-right": "1rem",
    "padding-left": "1rem",
    "padding-bottom": "1rem",
    "width": "auto",
}

layout = html.Div(
    [
        dcc.Upload(
            id="upload-image",
            children=html.Div([
                "Drag and Drop or ", 
                html.A("Select Files")
            ]),
            style={
                "width": "60%",
                "height": "400px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "10px",
                "textAlign": "center",
                "margin": "10px",
            },
            # Allow multiple files to be uploaded
            multiple=False
        ),
        html.Div(
            children=[html.H5("Waiting for image...")],
            id="info"),
        html.Div(
            id="output-image-upload",
        ),        
    ],
    style=CONTENT_STYLE,
)

def parse_contents(contents, filename):
    return html.Div([            
            # HTML images accept base64 encoded strings in the same format
            # that is supplied by the upload
            html.Img(
                src=contents,
                style={                    
                    "height": "auto",
                    "overflow": "hidden",
                    "object-fit": "cover",
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                    "width": "70%"
                },
            ),
            html.H5(filename),
            html.Button(id="run")

        ])

@app.callback(Output("upload-image","children"),
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