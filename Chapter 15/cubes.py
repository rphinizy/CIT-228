
import matplotlib.pyplot as plt

cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
plt.suptitle("My Numbers",c="orange",fontfamily="Bookman Old Style", fontsize="30")
plt.subplots_adjust(top=.8,wspace=1)
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,cubed)
plt.plot(inputVal,cubed, marker ='*',ls='--', lw='6',c="blue")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

pow=[]
for num in inputVal:
    pow.append(num*num)
plt.style.use("seaborn")       
ax2 = plt.subplot(1,2,2) 
ax2.plot(inputVal,pow)
plt.plot(inputVal,pow, c='red')
plt.title("Numbers Raised")
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()

plt.show()
