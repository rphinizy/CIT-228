import pandas as pd
import matplotlib.pyplot as plot



#use pandas to read file
dataFile = 'data/UFO.csv'
df = pd.read_csv(dataFile)

hour_of_day, duration=[], []

for row in df.values:
    date_string=row[0]
    seconds_string =float(row[5])
    seconds_string=int(seconds_string)

    #convert seconds to minutes
    seconds_string =seconds_string/60

    # clump duration data for a better view.. AKA manipulate till you get the answer you want. 
    if (seconds_string < 15):
        seconds_string = 15
    
    if (seconds_string < 30 and seconds_string >=15):
        seconds_string = 60
    
    if (seconds_string < 120 and seconds_string >=30):
        seconds_string = 100
    
    if (seconds_string < 250 and seconds_string >=120):
        seconds_string = 200
    
    if (seconds_string < 350 and seconds_string >=250):
        seconds_string = 300
    
    if (seconds_string < 500 and seconds_string >=350):
        seconds_string = 400
    
    if (seconds_string < 600 and seconds_string >=500):
        seconds_string = 500
    
    if (seconds_string < 700 and seconds_string >=600):
        seconds_string = 600
    
    if (seconds_string < 800 and seconds_string >=700):
        seconds_string = 700

    if (seconds_string < 900 and seconds_string >=800):
        seconds_string = 800
    
    if (seconds_string < 1000 and seconds_string >=900):
        seconds_string = 900

    if (seconds_string >1000):
        seconds_string = 1000
    

    duration.append(seconds_string)

    match len(date_string):
        case 16:
            hour_of_day.append(date_string[11:13])
        case 15:
             hour_of_day.append(date_string[10:12])
        case 14:
            hour_of_day.append(date_string[9:11])
    
    
   

data ={"Hour":hour_of_day,
        "Duration":duration
        }

dataFrame =pd.DataFrame(data=data)
dataFrame.plot.scatter(x = 'Hour', y = 'Duration', title="No Correlation between Time/Duration")

plot.show(block=True)

    
    


