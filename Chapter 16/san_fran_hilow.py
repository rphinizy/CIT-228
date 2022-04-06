import csv
from datetime import datetime
from tkinter import font
from matplotlib import pyplot as plt

filename='data/sanfran.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    #get high temps
    dates, highs, lows=[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high=int(row[3])
        low=int(row[4])
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

    #for index, column_header in enumerate(header_row):
        #print(index,column_header)
print(highs)

#plot highs
plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.scatter(dates, highs, c='red')
ax.scatter(dates, lows, c='blue')

#format plot
ax.set_title("San Francisco High low Temps", fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize =16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
   