#You have to run this script every time you run a new map, to make sure it is up to date

import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])


map = folium.Map(location=[38.59,-99.09], zoom_start=6, tiles="Mapbox Bright")


#create a feature group to be more organised
fg = folium.FeatureGroup(name="My Map")


for lt,ln in zip(lat,lon):
	fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

#this is like adding another layer for better organisation

map.add_child(fg)

map.save("Map1.html")

