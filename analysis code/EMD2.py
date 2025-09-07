from PyEMD import EEMD
import numpy as np
import pylab as plt

# Define signal
t = np.arange(0, 100, 0.1)

x = np.loadtxt('highnoise.txt',usecols=0)
x = np.reshape(x,(1000,1000))
x = np.average(x,axis=1)

y = np.loadtxt('highnoise.txt',usecols=1)
y = np.reshape(y,(1000,1000))
y = np.average(y,axis=1)

data = np.sqrt(x**2+y**2)

""" data = np.loadtxt('highnoise.txt',usecols=2)
data = np.reshape(data,(1000,500))
data = np.average(data,axis=1) """



# Assign EEMD to `eemd` variable
eemd = EEMD()

# Say we want detect extrema using parabolic method
emd = eemd.EMD
emd.extrema_detection="parabol"

# Execute EEMD on S
eIMFs = eemd.eemd(data, t)
nIMFs = eIMFs.shape[0]

# Plot results
plt.figure(figsize=(11,8))
plt.subplot(nIMFs+1, 1, 1)
plt.plot(t, data, 'r')
plt.ylabel("origin data")

for n in range(nIMFs):
    plt.subplot(nIMFs+1, 1, n+2)
    plt.plot(t, eIMFs[n], 'g')
    plt.ylabel("eIMF %i" %(n+1))
    plt.locator_params(axis='y', nbins=5)

plt.xlabel("Time [s]")
plt.tight_layout()
plt.savefig('eemd_example', dpi=120)
plt.show()