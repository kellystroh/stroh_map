# Import required libraries
import os
from random import randint

import plotly.plotly as py
import plotly.graph_objs as go

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)


# Put your Dash code here
df = pd.read_csv('world_travel.csv')
data = [ go.Scattergeo(
        lon = df[df.reason == i]['long'],
        lat = df[df.reason == i]['lat'],
        text = df[df.reason == i]['text'],
        mode = 'markers',
        marker = dict(
            size = 5,
            opacity = 1,
            reversescale = True,
            autocolorscale = False,
            # symbol = 'square',
            line = dict(width=.5, 
                        color='white')),
            name = str(i)
        ) for i in df.reason.unique() ]

layout = dict(
        title=go.layout.Title(text=""),
        colorbar = True,
        margin = dict(t = 0, b = 0, l = 0, r = 0),
        legend=go.layout.Legend(x=.2,y=-.05,
                                traceorder="normal",
                                orientation='h',
                                font=dict(family="times-new-roman",
                                          size=12,
                                          color="black")
                                ),
        geo = dict(
            scope='world',
            projection=dict( type='natural earth' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ))

fig = dict( data=data, layout=layout )    

app.layout  = html.Div([
    dcc.Graph(id='graph', figure=fig)
])


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)