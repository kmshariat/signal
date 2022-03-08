from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 1, 1000)
current = signal.square(2*np.pi*0.5*time) #This signal.squre command creates rectangular signal from sinusoidal signal

plt.title("Rectangular Wave") 
plt.xlabel("Time") #xlabel is used for labeling x axis
plt.ylabel("Current") #ylabel is used for labeling y axis

plt.plot(time, current, color="green")
plt.show()
