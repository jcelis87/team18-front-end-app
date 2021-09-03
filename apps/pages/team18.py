from apps.utils.get_data import API_URL
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

colors = {"background": "#111111", "text": "#7FDBFF"}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-top": "1px",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "width": "auto",
}
IMAGE_STYLE = {
    "border-radius": "60%",
    "height": "180px",
    "align": "right"    
}
BLANK = {
    "height": "auto"
}
TITLE = {
    #"background-color": "blue"
}

layout = html.Div([
        dbc.Row(
            html.H2("Equipo 18", style=TITLE), justify="center", style={"height":"80px"}
        ),
        dbc.Row(
            dbc.Col(html.Div(style=BLANK), width=12)
        ),
        dbc.Row([
                dbc.Col(
                    html.Img(src=API_URL+"/image/deniz", style=IMAGE_STYLE),
                    width=2
                ),                
                dbc.Col(
                    dcc.Markdown("""
                    #### Deniz Sáchez S.
                    Temática grupo interno de trabajo índices, DANE
                    Matemática, Universidad Nacional de Colombia (Bogotá)
                    Magister en Ciencias Estadística, Universidad Nacional de Colombia (Bogotá)

                    [Contactar en LinkedIn](https://www.linkedin.com/in/deniz-andrea-sanchez-segura-94242813a/?originalSubdomain=co)
                    """
                    ),
                    #width=3

                ),
                dbc.Col(
                    html.Div(style=BLANK), width=1
                ),
                dbc.Col(
                    html.Img(src=API_URL+"/image/josec", style=IMAGE_STYLE),
                    width=2
                ),
                dbc.Col(
                    dcc.Markdown("""
                    #### Jose Celis
                    CEO Appspring
                    MBA Rotman school of management, university of Toronto. 
                    Ingeniero industrial, economista, Universidad de los Andes

                    [Contactar en LinkedIn](https://www.linkedin.com/mwlite/in/jcelis87)
                    """
                    ),
                    #width=3
                )                
            ],
            justify="center"
        ),
        dbc.Row([
                dbc.Col(
                    html.Img(src=API_URL+"/image/sergio", style=IMAGE_STYLE),
                    width=2
                ),                
                dbc.Col(
                    dcc.Markdown("""
                    #### Sergio Sepúlveda
                    Profesor Asistente Universidad Francisco de Paula Santander, Cúcuta, Colombia. 
                    Candidato a doctor en Ingeniería Eléctrica y Computación, University of Delaware, Newark, DE, USA

                    [Contactar en LinkedIn](https://www.linkedin.com/in/sergio-sepúlveda-653724109/)
                    """
                    ),
                    #width=3

                ),
                dbc.Col(
                    html.Div(style=BLANK), width=1
                ),
                dbc.Col(
                    html.Img(src=API_URL+"/image/diego", style=IMAGE_STYLE),
                    width=2
                ),
                dbc.Col(
                    dcc.Markdown("""
                    #### Diego A. Hernández C.
                    Científico de datos, NUVU. 
                    Matemático, Universidad Nacional de Colombia (Bogotá). 
                    Ingeniero Catastral y Geodesta, Universidad Distrital Francisco José de Caldas

                    [Contactar en LinkedIn](https://www.linkedin.com/in/diego-a-hern%C3%A1ndez-casta%C3%B1eda-688842134/)
                    """
                    ),
                    #width=3
                )                
            ],
            justify="center"
        ),
        dbc.Row([
                dbc.Col(
                    html.Img(src=API_URL+"/image/camilo", style=IMAGE_STYLE),
                    width=2
                ),                
                dbc.Col(
                    dcc.Markdown("""
                    #### Camilo García Torres
                    Científico de datos, Big Bang Data. 
                    Bogota, Colombia. 
                    Ingeniero Mecánico de la Universidad de los Andes

                    [Contactar en LinkedIn](https://www.linkedin.com/in/camilo-garcia-27b178172/)
                    """
                    ),
                    #width=3

                ),
                dbc.Col(
                    html.Div(style=BLANK), width=1
                ),
                dbc.Col(
                    html.Img(src=API_URL+"/image/mario", style=IMAGE_STYLE),
                    width=2
                ),
                dbc.Col(
                    dcc.Markdown("""
                    #### John Mario Montoya Zapata
                    Analista de datos en Calidad del Aire, AMVA-SIATA. 
                    Ingeniero Cilvil, Universidad Nacional de Colombia (Medellín). 
                    Estudiante Maestría en Ingeniería-Recursos Hidráulicos, Universidad Nacional de Colombia (Medellín)

                    [Contactar en LinkedIn](https://www.linkedin.com/in/john-m-montoya-z-1a375a15b/)
                    """
                    ),
                    #width=3
                )                
            ],
            justify="center"
        )
    ],
    style=CONTENT_STYLE,
)
