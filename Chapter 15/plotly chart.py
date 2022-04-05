import plotly.graph_objects as go
from plotly import offline
import numpy as np 

# percentage of fast food consumption per day by different sexes and age groups    
#https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1
men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=age_range,
    y=men,
    name='Men',
    marker_color='lightblue'
))
fig.add_trace(go.Bar(
    x=age_range,
    y=women,
    name='Women',
    marker_color='pink'
))

fig.add_trace(go.Bar(
    x=age_range,
    y=total,
    name='Total',
    marker_color='lightgreen'
))

layout=fig.update_layout(
    title='Fast Food Consumption Per Day',
    title_font_color='orange',
    title_font_family="Raleway", 
    title_font_size=30,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Percentages',
        titlefont_size=16,
        tickfont_size=14,
    ),
    xaxis=dict(
        title='2013-2016',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
#fig.show()

offline.plot({'data': fig, 'layout':layout}, filename='plotly.html')