import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0,5,100) 
current = np.e**(time) #this is for exponential current

plt.title("Exponential Signal")
plt.xlabel("Time") #xlabel is used for labeling x axis
plt.ylabel("Current") #ylabel is used for labeling y axis

plt.plot(time,current, color = "red")
plt.show()
