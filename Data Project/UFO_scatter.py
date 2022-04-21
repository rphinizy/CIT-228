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
dataFrame.plot.scatter(x = 'Hour', y = 'Duration', title="Too much data to tell")

plot.show(block=True)
#duration.sort()
#print(duration)
#print(hour_of_day)
    
    
    


