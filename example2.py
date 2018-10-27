import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
import plotly.plotly as py
from plotly.graph_objs import *
from scipy.stats import rayleigh
from flask import Flask
import numpy as np
import pandas as pd
import os
import sqlite3
import datetime as dt

app = dash.Dash('streaming-wind-app')
server = app.server

app.layout = html.Div([

    html.Div([
        html.H2("Wind Speed Monitor"),
        html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png"),
    ], className='banner'),

    html.Div([
        html.Div([
            html.Div([
                html.H3("WIND SPEED (mph)")
            ], className='Title'),
            html.Div([
                dcc.Graph(id='wind-speed'),
            ], className='twelve columns wind-speed'),
            dcc.Interval(id='wind-speed-update', interval=3000, n_intervals=0),
        ], className='seven columns wind-histogram'),

        html.Div([
            html.Div([
                html.H3("WIND DIRECTION")
            ], className='Title'),
            dcc.Graph(id='wind-direction'),
        ], className='five columns wind-polar')


    ], className='row wind-histo-polar')
], style={'padding': '0px 10px 10px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "1000px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'})



@app.callback(Output('wind-speed', 'figure'), [Input('wind-speed-update', 'n_intervals')])
def gen_wind_speed(interval):
    now = dt.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour

    total_time = (hour * 3600) + (minute * 60) + (sec)

    con = sqlite3.connect("./Data/wind-data.db")
    df = pd.read_sql_query('SELECT Speed, SpeedError, Direction from Wind where\
                            rowid > "{}" AND rowid <= "{}";'
                            .format(total_time-100, total_time), con)

    trace = Scatter(
        y=df['Speed'],
        line=Line(
            color='#42C4F7'
        ),
        hoverinfo='skip',
        error_y=ErrorY(
            type='data',
            array=df['SpeedError'],
            thickness=1.5,
            width=2,
            color='#B4E8FC'
        ),
        mode='lines'
    )

    layout = Layout(
        height=450,
        xaxis=dict(
            range=[0, 100],
            showgrid=False,
            showline=False,
            zeroline=False,
            fixedrange=True,
            tickvals=[0, 25, 50, 75, 100],
            ticktext=['100', '75', '50', '25', '0'],
            title='Time Elapsed (sec)'
        ),
        yaxis=dict(
            range=[min(0, min(df['Speed'])),
                   max(45, max(df['Speed'])+max(df['SpeedError']))],
            showline=False,
            fixedrange=True,
            zeroline=False,
            nticks=max(6, round(df['Speed'].iloc[-1]/10))
        ),
        margin=Margin(
            t=45,
            l=50,
            r=50
        )
    )

    return Figure(data=[trace], layout=layout)


@app.callback(Output('wind-direction', 'figure'), [Input('wind-speed-update', 'n_intervals')])
def gen_wind_direction(interval):
    now = dt.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour

    total_time = (hour * 3600) + (minute * 60) + (sec)

    con = sqlite3.connect("./Data/wind-data.db")
    df = pd.read_sql_query("SELECT * from Wind where rowid = " +
                                         str(total_time) + ";", con)
    val = df['Speed'].iloc[-1]
    direction = [0, (df['Direction'][0]-20), (df['Direction'][0]+20), 0]

    trace = Scatterpolar(
        r=[0, val, val, 0],
        theta=direction,
        mode='lines',
        fill='toself',
        fillcolor='rgb(242, 196, 247)',
        line=dict(
            color='rgba(32, 32, 32, .6)',
            width=1
        )
    )
    trace1 = Scatterpolar(
        r=[0, val*0.65, val*0.65, 0],
        theta=direction,
        mode='lines',
        fill='toself',
        fillcolor='#F6D7F9',
        line=dict(
            color = 'rgba(32, 32, 32, .6)',
            width = 1
        )
    )
    trace2 = Scatterpolar(
        r=[0, val*0.3, val*0.3, 0],
        theta=direction,
        mode='lines',
        fill='toself',
        fillcolor='#FAEBFC',
        line=dict(
            color='rgba(32, 32, 32, .6)',
            width=1
        )
    )

    layout = Layout(
        autosize=True,
        width=275,
        margin=Margin(
            t=10,
            b=10,
            r=30,
            l=40
        ),
        polar=dict(
            bgcolor='#F2F2F2',
            radialaxis=dict(range=[0, 45],
                            angle=45,
                            dtick=10),
            angularaxis=dict(
                showline=False,
                tickcolor='white',
            )
        ),
        showlegend=False,
    )

    return Figure(data=[trace, trace1, trace2], layout=layout)


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/737dc4ab11f7a1a8d6b5645d26f69133d97062ae/dash-wind-streaming.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i"]


for css in external_css:
    app.css.append_css({"external_url": css})

if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })

if __name__ == '__main__':
    app.run_server()
