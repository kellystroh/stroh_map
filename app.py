'''import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('world_travel.csv')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Figure(data=go.Scattergeo(
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker_color = df['reason']
        ))
            ],
            'layout': go.Layout(
                geo_scope='world'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()'''

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()

df = pd.read_csv('world_travel.csv')

# df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

# scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
#     [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

# data = [ dict(
#         type = 'scattergeo',
#         # locationmode = 'USA-states',
#         lon = df['long'],
#         lat = df['lat'],
#         text = df['text'],
#         mode = 'markers',
#         marker = dict(
#             size = 5,
#             opacity = 0.8,
#             reversescale = True,
#             autocolorscale = False,
#             # symbol = 'square',
#             line = dict(
#                 width=1,
#                 color='white'
#             ),
#             # colorscale = scl,
#             # cmin = 0,
#             color = df['reason']
#             # cmax = df['cnt'].max(),
#             # colorbar=dict(
#             #     title="Incoming flightsFebruary 2011"
#             # )
#         ))]

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


# annotations = [dict(
  
#               # text I want to display. I used <br> to break it into two lines
#               text = 'All US storm events that caused more than $50k of economic damage,<br> from 2000 until today', 
              
#               # font and border characteristics
#               font = dict(color = '#FFFFFF', size = 14), borderpad = 10, 
              
#               # positional arguments
#               x = 0.05, y = 0.05, xref = 'paper', yref = 'paper', align = 'left', 
              
#               # don't show arrow and set background color
#               showarrow = False, bgcolor = 'black'
#               )]

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

# assigning the annotations to the layout
# layout['annotations'] = annotations

fig = dict( data=data, layout=layout )    
# fig.update_layout(legend_orientation="h")

app.layout  = html.Div([
    dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)