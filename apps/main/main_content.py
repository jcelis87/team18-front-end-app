from apps.pages.eda import CONTENT_STYLE
import dash_html_components as html
import dash_core_components as dcc

CONTENT_STYLE={
    "height": "100vh",
    "background-color": "white"
}

layout = html.Div(
    id="page-content",
    className="",
    children=[],
    style=CONTENT_STYLE
)
