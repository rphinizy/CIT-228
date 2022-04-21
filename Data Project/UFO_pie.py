import numpy as np

import pandas as pd

import matplotlib.pyplot as plot


#use pandas to read file
dataFile = 'data/UFO.csv'
df = pd.read_csv(dataFile)

lats, lons=[],[]
north_america=0
south_america=0
europe=0
africa=0
total=0


for row in df.values:
    lat=int(row[9])
    lon=int(row[10])
    lons.append(lon)
    lats.append(lat)
    # count sightings north america
    if (lat <=71 and lat >=13):
        if(lon>-156 and lon <-60):
            north_america+=1
    
    #south america
    if(lat <= 10 and lat>=-40):
        if(lon >-80 and lon <-34):
            south_america+=1

    #africa sightings
    if(lat <= 36 and lat>=-33):
        if(lon >-80 and lon <-34):
            africa+=1
    
    #europe sightings
    if(lat <= 64 and lat>=36):
        if(lon >-9 and lon <25):
            europe+=1

    total+=1
    



dataframe = pd.DataFrame({'Region': ['north america','south america', 'africa', 'europe'],
                          'sightings': [north_america,south_america, africa, europe]})
  
# Plotting the pie chart for above dataframe
dataframe.groupby(['Region']).sum().plot(kind='pie', y='sightings', title="SIGHTINGS BY REGION", ylabel="")
plot.show()



#equator.sort()
#print(north)
#print(south)
#print(equator)
#print(north_equator)
#print(south_equator)
#print(near_equator)
#print(lats)
print("US LATS")
print(north_america)
print(south_america)
print(africa)
print(europe)

    
    