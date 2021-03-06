import json
import dash
import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash.dependencies import Output, Input, State
import dash_table

import pandas as pd

from app import app
from apps.utils.get_data import get_all_geonames
from apps.utils.create_data_frame import (
    create_data_frame,
    get_map_data,
    create_data_frame_geojson,
)
from apps.components import table



allNames = get_all_geonames()
df_allNames = create_data_frame(allNames)

MAP_ID = "map"
MARKER_GROUP_ID = "marker-group"
COORDINATE_CLICK_ID = "coordinate-click-id"

MAP_STYLE = {
    "width": "auto",
    "height": "60vh",
}

CONTENT_STYLE = {
    "margin-left": "16rem",
    # "margin-top": "1rem",
    "margin-right": "1rem",
    "padding-left": "1rem",
    "padding-bottom": "1rem",
    "width": "auto",
}

PAGE_SIZE = 10

geographicNames = get_map_data(df_allNames)

geojson = dlx.dicts_to_geojson(
    [{**c, **dict(tooltip=c["geographic_name"])} for c in geographicNames],
    # geographicNames,
    lat="latitude",
    lon="longitude",
)

# print(geojson)

layout = html.Div(
    id="",
    className="",
    children=[
        dl.Map(
            center=[3.723537853558591, -75.48487696174067],
            zoom=10,
            children=[
                dl.TileLayer(
                    # url="http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}"
                ),
                dl.LayerGroup(id=MARKER_GROUP_ID),
                dl.GeoJSON(
                    data=geojson,
                    id="geojson",
                    cluster=True,
                    zoomToBoundsOnClick=True,
                    superClusterOptions={"radius": 100},
                ),
                dl.GestureHandling(),
            ],
            id=MAP_ID,
            style=MAP_STYLE,
        ),
        html.P("Click en el mapa para ver las coordenadas:"),
        html.Div(id=COORDINATE_CLICK_ID),
        html.Div(html.P(""), id="state"),
        html.Div(
            html.P(""),
            id="name-id-row",
        ),
        html.Div(
            dash_table.DataTable(
                id="table",
                columns=[{"name": i, "id": i} for i in df_allNames.columns],
                # data=df_allNames.to_dict("records"),
                page_current=0,
                # page_size=PAGE_SIZE,
                # page_action="custom",
                data=df_allNames.to_dict("records"),
                style_data_conditional=[],
                style_table={"height": "30vh", "overflowY": "auto"},
            )
        ),
    ],
    style=CONTENT_STYLE,
)

@app.callback(Output(MARKER_GROUP_ID, "children"), [Input(MAP_ID, "click_lat_lng")])
def set_marker(x):
    if not x:
        return None
    return dl.Marker(position=x, children=[dl.Tooltip("Test")])


@app.callback(Output(COORDINATE_CLICK_ID, "children"), [Input(MAP_ID, "click_lat_lng")])
def click_coord(e):
    if not e:
        return "-"
    return json.dumps(e)


@app.callback(
    Output("table", "style_data_conditional"),
    [Input("geojson", "hover_feature")],
    [State("table", "data")],
)
def state_hover(feature, data):
    if feature is not None:
        styles = []
        if feature["properties"]["cluster"]:
            raise dash.exceptions.PreventUpdate
        try:
            marker_id = df_allNames[
                df_allNames["geographic_name"] == feature["properties"]["tooltip"]
            ]["name_id"].values      

            styles = [
                {
                    "if": {
                        "filter_query": "{{name_id}} = {value}".format(
                            name_id=df_allNames[df_allNames["name_id"] == marker_id[0]][
                                "name_id"
                            ].values[0],
                            value=marker_id[0],
                        ),
                    },
                    "backgroundColor": "#FF4136",
                    "color": "white",
                },
            ]
        except (KeyError, IndexError):
            print("wrong key")        

        return styles

@app.callback(
    Output("name-id-row", "children"),
    [Input("table", "active_cell")],
)
def get_active_cell_value(active_cell):

    print(active_cell)
    if active_cell:
        return [active_cell["row"], active_cell["column_id"]]