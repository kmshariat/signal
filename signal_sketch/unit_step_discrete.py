import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0,20,10)
current = 1 + time*0 #this is for dc current of magnitide 2

plt.title("Unit Step Function : Discrete")
plt.xlabel("Time") #xlabel is used for labeling x axis
plt.ylabel("Current") #ylabel is used for labeling y axis

plt.yticks([1]) #this removes ticks in the y axis other than 1

plt.plot(time, current, "go")
plt.show()
