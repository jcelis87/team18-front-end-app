# region Imports
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dotenv import load_dotenv

import dash_auth
from dash.dependencies import Input, Output

# dash instance
from app import app, server

# callbacks import
from callbacks import register_callbacks

# Dash custom modules
from apps.main import main_header, main_sidebar, main_content, main_footer
# endregion

USERNAMEINFO = [['igac','Team#18']]
auth = dash_auth.BasicAuth(app,USERNAMEINFO)

#main layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        main_header.layout,
        main_sidebar.layout,
        main_content.layout,
        #main_footer.layout
    ],
)

# Callbacks register
register_callbacks(app)

if __name__ == "__main__":
    load_dotenv()
    app.run_server(host="0.0.0.0", debug=False, port=8050, dev_tools_props_check=False)