from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0,8,100)
current = signal.unit_impulse(100)

plt.title("Unit Impulse Function")
plt.xlabel("Time")
plt.ylabel("Current")

plt.plot(time,current, "r")
plt.show()
