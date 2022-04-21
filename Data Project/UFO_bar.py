import pandas as pd
import matplotlib.pyplot as plot


#use pandas to read file
dataFile = 'data/UFO.csv'
df = pd.read_csv(dataFile)

dates=[]
counterA =0
counterB=0
counterC=0
counterD=0
counterE=0
counterF=0
counterG=0
counterH=0
counterI=0

for row in df.values:
    date_string=row[0]
    # slice the time stamp from date
    remove_time=date_string[0:-6]

    #match case to slice month and date
    match len(remove_time):
        case 8:
            year_only=remove_time[4:8]
        case 9:
            year_only=remove_time[5:9]
        case 10:
            year_only=remove_time[6:10]
    
    #current_date = datetime.strptime(year_only, "%Y")
    current_date = year_only

    #match case to determine number of sightings in a specific year
    match current_date:
        case "1965":
            counterA +=1
        case "1976":
            counterB +=1
        case "1980":
            counterC +=1
        case "1990":
            counterD +=1
        case "2000":
            counterE +=1
        case "2011":
            counterF +=1
        case "2012":
            counterG +=1
        case "2013":
            counterH +=1
        case "2014":
            counterI +=1
    
    
    
# CODE NO LONGER NEEDED BUT KEEPING FOR REFERENCE
#*****************************************************

    #dates.append(current_date)

# most recent signting in data set - 2014
# earliest sighting in data set - 1906
#dates.sort(reverse=True)
#graph 1965, 1976, 1980, 1990, 2000, 2014

#print(dates)
#print(years)
#print(occurences)

#*****************************************************

# Make the Pandas Bar graph

data ={"Year":["1965","1976", "1980", "1990", "2000", "2011", "2012", "2013", "2014"],
        "Occurences":[counterA, counterB, counterC, counterD, counterE, counterF, counterG, counterH, counterI]
        }

dataFrame =pd.DataFrame(data=data)

dataFrame.plot.bar(x="Year", y="Occurences", rot=0, title="Number of UFO Sightings by Year")

plot.show(block=True)