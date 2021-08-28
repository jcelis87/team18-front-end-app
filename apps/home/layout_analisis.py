import dash_html_components as html
import dash_core_components as dcc

from apps.main import main_nav, main_content


layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        main_nav.layout,
        main_content.layout,
        #main_footer.layout,

    
    ])