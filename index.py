# Dash basic libraries
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# dash instance
from app import app, server

# callbacks import
from callbacks import register_callbacks

# Dash custom modules
from apps.main import main_nav, main_content

from apps.home import layout_analisis,layout_home, layout_imagen


# main layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        main_nav.layout,
        main_content.layout,
        #main_footer.layout,

    ]
    
)

# Callbacks register
register_callbacks(app)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == 'apps/home/layout_analisis':
        return layout_analisis.layout
    if pathname == 'apps/home/layout_imagen':
        return layout_imagen.layout
    if pathname == 'apps/home/layout_home':
        return layout_home.layout




if __name__ == "__main__":
    app.run_server(debug=True)
