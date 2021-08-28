# import json
# import dash
# import dash_html_components as html
# from dash.dependencies import Output, Input, State
# import dash_table

# import pandas as pd

# from app import app
# from apps.utils.get_data import get_all_geonames
# from apps.utils.create_data_frame import create_data_frame

# # Get Data from Geonames API


# allNames = get_all_geonames()

# df_allNames = create_data_frame(allNames)


# CONTENT_STYLE = {
#     "margin-left": "1rem",
#     "margin-top": "1rem",
#     "margin-right": "1rem",
#     "padding": "1rem 1rem",
# }

# PAGE_SIZE = 10

# layout = html.Div(
#     id="",
#     className="",
#     children=[
#         html.Div(
#             dash_table.DataTable(
#                 id="table",
#                 columns=[{"name": i, "id": i} for i in df_allNames.columns],
#                 # data=df_allNames.to_dict("records"),
#                 page_current=0,
#                 page_size=PAGE_SIZE,
#                 page_action="custom",
#             )
#         ),
#         html.Div(
#             html.P("Hola"),
#             id="name-id-row",
#         ),
#     ],
#     style=CONTENT_STYLE,
# )


# @app.callback(
#     Output("table", "data"),
#     Input("table", "page_current"),
#     Input("table", "page_size"),
# )
# def update_table(page_current, page_size):
#     return df_allNames.iloc[
#         page_current * page_size : (page_current + 1) * page_size
#     ].to_dict("records")


# @app.callback(
#     Output("name-id-row", "children"),
#     [Input("table", "active_cell")],
# )
# def get_active_cell_value(active_cell):

#     print(active_cell)
#     if active_cell:
#         return [active_cell["row"], active_cell["column_id"]]
