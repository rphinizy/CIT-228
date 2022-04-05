import matplotlib.pyplot as plt  
import numpy as np 
# percentage of fast food consumption per day by different sexes and age groups    
#https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1
men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]
barWidth=.25

br1 = np.arange(len(age_range)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2]

plt.xticks([r + barWidth for r in range(len(age_range))],age_range) 
plt.suptitle("Fast Food Consumption Per Day",c="orange",fontfamily="Bookman Old Style", fontsize="16")

plt.bar(br1, men, color ='lightblue', width=barWidth, label="Men") 
plt.bar(br2,women, color="pink",  width=barWidth, label="Women")
plt.bar(br3,total, color="lightgreen", width=barWidth,  label="Total")
  
plt.ylabel("Percentages") 
plt.xlabel("2013-2016") 
plt.legend(loc="best")
plt.show() 
