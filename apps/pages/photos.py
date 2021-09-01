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

# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'geo_database_sample_50.csv')

PROJECT_FOLDER = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

UPLOAD_DIRECTORY = os.path.join(PROJECT_FOLDER, "images")

print(UPLOAD_DIRECTORY)

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


# padding for the page content
CONTENT_STYLE = {
    "margin-left": "16rem",
    # "margin-top": "1rem",
    "margin-right": "1rem",
    "padding-left": "1rem",
    "padding-bottom": "1rem",
    "width": "auto",
}

layout = html.Div(
    [
        dcc.Upload(
            id="upload-image",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "50%",
                "height": "300px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "10px",
                "textAlign": "center",
                "margin": "10px",
            },
            # Allow multiple files to be uploaded
            multiple=True,
        ),
        html.Div(
            id="output-image-upload",
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style=CONTENT_STYLE,
)


def parse_contents(contents, filename, date):
    return html.Div(
        [
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),
            # HTML images accept base64 encoded strings in the same format
            # that is supplied by the upload
            html.Img(
                src=contents,
                style={
                    "width": "auto",
                    "height": "800px",
                    "overflow": "hidden",
                    "object-fit": "cover",
                },
            ),
            html.Hr(),
            html.Div("Raw Content"),
            html.Pre(
                contents[0:200] + "...",
                style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
            ),
        ]
    )


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))
        
    send_file(os.path.join(UPLOAD_DIRECTORY, name))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("output-image-upload", "children"),
    Input("upload-image", "contents"),
    State("upload-image", "filename"),
    State("upload-image", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children


@app.callback(
    Output("file-list", "children"),
    [Input("upload-image", "filename"), Input("upload-image", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]
