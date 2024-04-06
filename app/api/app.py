import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import base64
from io import BytesIO
import sys
import numpy as np
from os.path import dirname, abspath
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Adjust the system path to access your custom modules
d = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(d)

from fastStruct.fem.system import SystemElements

# Configure Matplotlib to use a font with a wider range of glyphs
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif']

def create_system_elements():
    """Function to configure and solve the structural system."""
    ss = SystemElements()
    ss.add_element([[0, 0], [2, 0]])
    ss.add_element([4, 0])
    ss.add_element([6, 0])
    ss.add_support_fixed([1, 4])
    ss.moment_load([2, 3], [20, -20])
    ss.solve()
    return ss

def fig_to_uri(fig):
    """Convert Matplotlib figure to URI."""
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    plt.close(fig)  # Close the figure to prevent memory leakage
    buf.seek(0)
    base64_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    return f'data:image/png;base64,{base64_image}'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Structure Analysis Result"),
    # Flex container for all columns
    html.Div([
        dbc.Col(html.Div([html.H2("Structure"), html.Img(id='structure-image', style={'width': '100%', 'padding': '10px'})]), width=6),
        dbc.Col(html.Div([html.H2("Reaction Force"), html.Img(id='reaction-force-image', style={'width': '100%', 'padding': '10px'})]), width=6),
        dbc.Col(html.Div([html.H2("Bending Moment"), html.Img(id='bending-moment-image', style={'width': '100%', 'padding': '10px'})]), width=6),
        dbc.Col(html.Div([html.H2("Displacement"), html.Img(id='displacement-image', style={'width': '100%', 'padding': '10px'})]), width=6),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),
], fluid=True)

STANDARD_FIGSIZE = (10, 6)

@app.callback(
    Output('structure-image', 'src'),
    Input('structure-image', 'id')
)
def update_structure_image(_):
    ss = create_system_elements()
    fig = ss.show_structure(show=False, figsize=STANDARD_FIGSIZE)
    return fig_to_uri(fig)

@app.callback(
    Output('reaction-force-image', 'src'),
    Input('reaction-force-image', 'id')
)
def update_reaction_force_image(_):
    ss = create_system_elements()
    fig = ss.show_reaction_force(show=False, figsize=STANDARD_FIGSIZE)
    return fig_to_uri(fig)

@app.callback(
    Output('bending-moment-image', 'src'),
    Input('bending-moment-image', 'id')
)
def update_bending_moment_image(_):
    ss = create_system_elements()
    fig = ss.show_bending_moment(show=False, figsize=STANDARD_FIGSIZE)
    return fig_to_uri(fig)

@app.callback(
    Output('displacement-image', 'src'),
    Input('displacement-image', 'id')
)
def update_displacement_image(_):
    ss = create_system_elements()
    fig = ss.show_displacement(show=False, figsize=STANDARD_FIGSIZE)
    return fig_to_uri(fig)




if __name__ == '__main__':
    app.run_server(debug=True)
