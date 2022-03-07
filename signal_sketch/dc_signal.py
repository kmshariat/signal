import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0,2,100)
current = 5000 + time*0 #this is for dc current of magnitide 2

plt.title("DC Signal")
plt.xlabel("Time") #xlabel is used for labeling x axis
plt.ylabel("Current") #ylabel is used for labeling y axis

plt.plot(time, current)
plt.show()
