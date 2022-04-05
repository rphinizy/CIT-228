import matplotlib.pyplot as plt  

labels = 'PNG', 'JPG', 'SVG', 'GIF','OTHER'
numImg = [376, 348, 153, 104,19]
explode = (.1, 0, 0, 0,0)  
wedgeColors=('lightgreen','lightblue','brown','pink','tan')

fig1, ax1 = plt.subplots()
ax1.pie(numImg, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=-45, colors=wedgeColors)
ax1.axis('equal')  
plt.suptitle("Popular Graphic Formats on the Web")

plt.show()