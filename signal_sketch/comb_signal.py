#Sampling function or comb function

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

time = [] #creating an array to store different values of time

for i in range(10):
  time.append(np.linspace(i,8,100)) #defining time with increase of 1

current = signal.unit_impulse(100) 

plt.title("Unit Impulse Function")
plt.xlabel("Time")
plt.ylabel("Current")

for j in range(10):
  plt.plot(time[j], current, "r") #plotting all the impulse functions
plt.show()
