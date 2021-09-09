import json
import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash.dependencies import Output, Input, State
import dash_table
import requests

import pandas as pd

from app import app
from apps.utils.get_data import (
    get_all_geonames,
    get_all_coordinates,
    get_all_boundaries,
    get_all_image_boundaries,
    get_image_url,
)
from apps.utils.create_data_frame import (
    create_data_frame,
    get_map_data,
    create_data_frame_geojson,
)
from apps.components import table


IMAGE_GROUP = "1"
MAP_ID = "map"
MARKER_GROUP_ID = "marker-group"
COORDINATE_CLICK_ID = "coordinate-click-id"
API_URL = os.getenv("API_URL")


allCoordinates = get_all_coordinates("0")
df_allCoordinates = create_data_frame_geojson(allCoordinates)
allCoordinates = df_allCoordinates.to_dict("records")

geojson = dlx.dicts_to_geojson(
    [{**c, **dict(tooltip=c["toponimo_ocr"])} for c in allCoordinates],
    # geographicNames,
    lat="centroide_latitud",
    lon="centroide_longitud",
)

image_bounds = requests.get(API_URL + "/img_corners").json()

image_bounds = [
    [
        image_bounds["upper_left"]["latitude"],
        image_bounds["upper_left"]["longitude"],
    ],
    [
        image_bounds["lower_right"]["latitude"],
        image_bounds["lower_right"]["longitude"],
    ],
]

image_url = API_URL + "/image/0"
print(image_url)

# get the boundaries of the img_to_process
allBoundaries = get_all_boundaries("0")
polygon_boundaries = allBoundaries["status"]

polygon = dl.Polygon(positions=polygon_boundaries)


MAP_STYLE = {
    "width": "auto",
    "height": "60vh",
    "display": "block",
}

CONTENT_STYLE = {
    "margin-left": "16rem",
    # "margin-top": "1rem",
    "margin-right": "1rem",
    "padding-left": "1rem",
    "padding-bottom": "1rem",
    "width": "auto",
}

layout = html.Div(
    id="",
    className="",
    children=[        
        html.Div(
            [
                dl.Map(
                    [
                        dl.LayersControl(
                            dl.Overlay(
                                dl.LayerGroup(polygon), name="polygon", checked=True
                            ),
                        ),
                        # dl.LayerGroup(id=MARKER_GROUP_ID),
                        # dl.GestureHandling(),
                        dl.ImageOverlay(
                            opacity=0.7, url=image_url, bounds=image_bounds
                        ),
                        dl.TileLayer(),
                        dl.GeoJSON(data=geojson, id="geojson"),
                    ],
                    bounds=image_bounds,
                    style=MAP_STYLE,
                    id=MAP_ID,
                ),
                html.Div(
                    dash_table.DataTable(
                        id="table",
                        columns=[
                            {"name": i, "id": i} for i in df_allCoordinates.columns
                        ],
                        page_current=0,
                        data=df_allCoordinates.to_dict("records"),
                        style_data_conditional=[],
                        style_table={"height": "30vh", "overflowY": "auto"},
                    )
                ),
            ],
            id="map-table",
        ),
    ],
    style=CONTENT_STYLE,
)


# @app.callback(
#     dash.dependencies.Output("map-table", "children"),
#     [dash.dependencies.Input("images-dropdown", "value")],
# )
# def update_image_output(value):
#     # Get Data from Geonames API

#     IMAGE_GROUP = value

#     allCoordinates = get_all_coordinates(IMAGE_GROUP)
#     df_allCoordinates = create_data_frame_geojson(allCoordinates)
#     allCoordinates = df_allCoordinates.to_dict("records")

#     geojson = dlx.dicts_to_geojson(
#         [{**c, **dict(tooltip=c["toponimo_ocr"])} for c in allCoordinates],
#         # geographicNames,
#         lat="centroide_latitud",
#         lon="centroide_longitud",
#     )

#     image_bounds = get_all_image_boundaries(IMAGE_GROUP)
#     image_bounds = image_bounds["status"]

#     image_bounds = [
#         [
#             image_bounds["upper_left"]["latitude"],
#             image_bounds["upper_left"]["longitude"],
#         ],
#         [
#             image_bounds["lower_right"]["latitude"],
#             image_bounds["lower_right"]["longitude"],
#         ],
#     ]

#     image_url = get_image_url(IMAGE_GROUP)

#     allBoundaries = get_all_boundaries(IMAGE_GROUP)
#     polygon_boundaries = allBoundaries["status"]

#     polygon = dl.Polygon(positions=polygon_boundaries)

#     return html.Div(
#         [
#             dl.Map(
#                 [
#                     dl.LayersControl(
#                         dl.Overlay(
#                             dl.LayerGroup(polygon), name="polygon", checked=True
#                         ),
#                     ),
#                     # dl.LayerGroup(id=MARKER_GROUP_ID),
#                     # dl.GestureHandling(),
#                     dl.ImageOverlay(opacity=0.7, url=image_url, bounds=image_bounds),
#                     dl.TileLayer(),
#                     dl.GeoJSON(data=geojson, id="geojson"),
#                 ],
#                 bounds=image_bounds,
#                 style=MAP_STYLE,
#             ),
#             dash_table.DataTable(
#                 id="table",
#                 columns=[{"name": i, "id": i} for i in df_allCoordinates.columns],
#                 page_current=0,
#                 data=df_allCoordinates.to_dict("records"),
#                 style_data_conditional=[],
#                 style_table={"height": "30vh", "overflowY": "auto"},
#             ),
#         ]
#     )
