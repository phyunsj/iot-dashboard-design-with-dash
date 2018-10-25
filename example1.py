import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.graph_objs import *
from dash.dependencies import Input, Output
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: Node-RED Example
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Interval(id='graph-update', interval=3000, n_intervals=0)
])

@app.callback( Output('example-graph', 'figure'),[Input('graph-update', 'n_intervals')])
def gen_graph_update(interval):

    trace = [
                {'x': [ 1,2,3], 'y': [random.randint(1,5), random.randint(1,5), random.randint(1,5)], 'type': 'bar', 'name': 'SF'},
                {'x': [1,2,3], 'y': [random.randint(1,5), random.randint(1,5), random.randint(1,5)], 'type': 'bar', 'name': 'Montreal'},
            ]
    layout = Layout(
        title='Dash Data Visualization'
    )
    return { 'data' : trace , 'layout' : layout }

if __name__ == '__main__':
    app.run_server(debug=False)