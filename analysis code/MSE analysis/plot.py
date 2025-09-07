import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['science', 'notebook'])
plt.figure(figsize=(12,7))

x1 = np.loadtxt("mseoutput.txt", skiprows=1, usecols=(0))
y1 = np.loadtxt("mseoutput.txt", skiprows=1, usecols=(1))

x2 = np.loadtxt("mseoutput_1_f_noise.txt", skiprows=1, usecols=(0))
y2 = np.loadtxt("mseoutput_1_f_noise.txt", skiprows=1, usecols=(1))

x3 = np.loadtxt("mseoutput_vic.txt", skiprows=1, usecols=(0))
y3 = np.loadtxt("mseoutput_vic.txt", skiprows=1, usecols=(1))


plt.plot(x1,y1,'o-')
plt.plot(x2,y2,'o-')
plt.plot(x3,y3,'o-')
plt.show()
