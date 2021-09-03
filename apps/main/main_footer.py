import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


FOOTER_STYLE = {
    "position": "sticky",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "3rem",
    "background-color": "#303d4e",
    "color": "#ffffff",
    "margin-left": "3rem"
}

info_general = dcc.Markdown("""
            **Acknowledgements**

            We want to acknowledge credit to Rodolfo Mesa and Diego Solarte
            for providing continuos feedback and a template for the Dash application
            and the FastAPI.

            All rights reserved &copy; 2021.
            """
        )


layout= html.Div([
        dbc.Row([
            dbc.Col(info_general, width=12)            
        ])
    ],     
    className="footer",
    style=FOOTER_STYLE
)