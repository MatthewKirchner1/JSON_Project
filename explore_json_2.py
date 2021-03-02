import json
import plotly

infile = open("eq_data_1_day_m1.json", "r")

outfile = open("readable_eq_data.json", "w")

# Converts the data to something pthon can read

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

"""
print(eq_data["features"][0]["properties"]["mag"])
"""

list_of_eqs = eq_data["features"]

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

mylayout = {}

mylayout["title"] = "Global Earthquakes"

fig = {"data": data, "layout": mylayout}

offline.plot(fig, filename="global_earthquakes.html")
