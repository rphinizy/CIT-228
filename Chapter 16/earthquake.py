import json
import plotly.graph_objects as go
from plotly import offline
import pandas as pd

filename ='data/query.geojson.json'
with open(filename) as f:
    all_eq_data=json.load(f)

readable_file ='data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent= 4)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats, hover_texts =[],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon =eq_dict['geometry']['coordinates'][0]
    lat =eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#print(mags[:10])
#print(lons[:5])
#print(lats[:5])

#Map the earthquakes

fig = go.Figure(data=go.Scattergeo(
    locationmode = 'USA-states',
    lon = lons,
    lat = lats,
    text = hover_texts,
    mode = 'markers',
        marker = dict(
            size = [5*mag for mag in mags],
            ),
))

fig.update_layout(
        title = 'US EarthQuakes past 30 days',
        geo = dict(
            scope='usa',
            showland = True,
            landcolor = "wheat",
            subunitcolor = "red",
            countrycolor = "black",
            countrywidth = 1,
            subunitwidth = 1
        ),
    )
offline.plot(fig, filename='US_earthquaks_30days.html')
