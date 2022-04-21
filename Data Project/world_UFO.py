import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename='data/UFO.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    lons, lats=[],[]

    for row in reader:
        lat=row[9]
        lon=float(row[10])
        lats.append(lat)
        lons.append(lon)


data =[{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size': 2,
    }
}]

my_layout =Layout(
    title = 'WORLD UFO SIGHTINGS 1906-2014',
    geo = dict(
            showland = True,
            landcolor = "wheat",
            subunitcolor = "red",
            countrycolor = "black",
            countrywidth = 1,
            subunitwidth = 1
        ),
)

fig={'data': data, 'layout': my_layout}


offline.plot(fig, filename='World_Wide_UFO_Sightings.html')
