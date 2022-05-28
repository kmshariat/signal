import numpy as np
import matplotlib.pyplot as plt

n = np.arange(50); #this defines how many defined value we want on our discrete signal e.g. the value of n
dt = 0.07/50 #this is our sampling rate
x = np.sin(2*np.pi*50*n*dt)**2+np.sin(2*np.pi*100*n*dt+1)**2+np.sin(np.pi*25*n*dt+3)**2 #this is our function or signal with respect to time

plt.xlabel('n'); #labels
plt.ylabel('x[n]'); #labels

plt.stem(n, x); #plt.stem for plotting discrete signals 
