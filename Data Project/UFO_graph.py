import pandas as pd
import matplotlib.pyplot as plot


#use pandas to read file
dataFile = 'data/UFO.csv'
df = pd.read_csv(dataFile)


#hold monthly counts for year 2012
jan, feb, mar, april, may, june, july, aug, sep, oct, nov, dec=0,0,0,0,0,0,0,0,0,0,0,0
#hold monthyly counts for year 2011
jan2, feb2, mar2, april2, may2, june2, july2, aug2, sep2, oct2, nov2, dec2 =0,0,0,0,0,0,0,0,0,0,0,0
#hold monthyly counts for year 2010
jan3, feb3, mar3, april3, may3, june3, july3, aug3, sep3, oct3, nov3, dec3 =0,0,0,0,0,0,0,0,0,0,0,0


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
    

    current_date = year_only

    #match cases to determine number of sightings in a specific year
    if(current_date=="2012"):
        match remove_time[0:2]:
            case"1/": jan+=1 
            case"2/": feb+=1
            case"3/": mar+=1
            case"4/": april+=1
            case"5/": may+=1
            case"6/": june+=1
            case"7/": july+=1
            case"8/": aug+=1
            case"9/": sep+=1
            case"10": oct+=1
            case"11": nov+=1
            case"12": dec+=1

    if(current_date=="2011"):
        match remove_time[0:2]:
            case"1/": jan2+=1 
            case"2/": feb2+=1
            case"3/": mar2+=1
            case"4/": april2+=1
            case"5/": may2+=1
            case"6/": june2+=1
            case"7/": july2+=1
            case"8/": aug2+=1
            case"9/": sep2+=1
            case"10": oct2+=1
            case"11": nov2+=1
            case"12": dec2+=1

    if(current_date=="2010"):
        match remove_time[0:2]:
            case"1/": jan3+=1 
            case"2/": feb3+=1
            case"3/": mar3+=1
            case"4/": april3+=1
            case"5/": may3+=1
            case"6/": june3+=1
            case"7/": july3+=1
            case"8/": aug3+=1
            case"9/": sep3+=1
            case"10": oct3+=1
            case"11": nov3+=1
            case"12": dec3+=1
     
 

first_monthy_sightings=[jan, feb, mar, april, may, june, july, aug, sep, oct, nov, dec]
second_monthy_sightings=[jan2, feb2, mar2, april2, may2, june2, july2, aug2, sep2, oct2, nov2, dec2]
third_monthy_sightings=[jan3, feb3, mar3, april3, may3, june3, july3, aug3, sep3, oct3, nov3, dec3]




data ={"month":["Jan", "Feb", "Mar","April","May","June","July","Aug","Sep","Oct","Nov","Dec"],
        "2012":first_monthy_sightings,
        "2011":second_monthy_sightings,
        "2010":third_monthy_sightings
        }

dataFrame =pd.DataFrame(data=data)
dataFrame.plot(x = 'month', y = ['2012', '2011', '2010'], title="2012 Sightings by Month", ylabel="SIGHTINGS", xlabel="")

plot.show(block=True)
