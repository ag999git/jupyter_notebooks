%matplotlib inline  ## Remove this line if not on Jupyter Notebook
# Author Anurag Gupta  ## Email :- 999.anuraggupta@gmail.com
import pandas as pd
import folium
from folium.plugins import HeatMap
fpath = r'https://raw.githubusercontent.com/ag999git/data/master/volerup.txt'
df = pd.read_csv(fpath, sep='\t', error_bad_lines= False)  
df1 = df.dropna(subset = ['Latitude', 'Longitude', 'TOTAL_DEATHS'])
init_loc = [0.7893, 113.9213]
m = folium.Map(location = init_loc, zoom_start = 5)
my_data = list(zip(df1.Latitude.values, df1.Longitude.values, df1.TOTAL_DEATHS.values))

max_death = int(df1['TOTAL_DEATHS'].max())
heat_map_deaths = HeatMap(my_data, 
                         min_opacity = 0.1,
                          max_val = max_death,
                         radius = 20,
                         blur = 20,
                         max_zoom = 2)
m.add_child(heat_map_deaths)
m
