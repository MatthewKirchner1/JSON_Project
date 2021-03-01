import json
import plotly

infile = open("US_fires_9_14.json", "r")

outfile = open("readable_US_fires_9_14_data.json", "w")

# Converts the data to something pthon can read

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

list_of_fires = fire_data

brights, lons, lats = [], [], []

for i in list_of_fires:

    bright = i["brightness"]
    lon = i["longitude"]
    lat = i["latitude"]

    if bright >= 450:

        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

print(brights[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

max_bright = max(brights)
print(max_bright)


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": 10,
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]


mylayout = {}

mylayout["title"] = "US Fires - 9/14/2020 through 9/20/2020"

fig = {"data": data, "layout": mylayout}

offline.plot(fig, filename="US_fires_9_14.html")