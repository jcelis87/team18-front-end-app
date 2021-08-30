# Dash basic libraries
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# dash instance
from app import app, server

# callbacks import
from callbacks import register_callbacks

# Dash custom modules
from apps.main import main_header, main_sidebar, main_content, main_footer


# main layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        main_header.layout,
        main_sidebar.layout,
        main_content.layout,
        # main_footer.layout,
    ],
)

# Callbacks register
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
