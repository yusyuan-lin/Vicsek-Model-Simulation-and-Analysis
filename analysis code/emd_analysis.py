import matplotlib.pyplot as plt
import numpy as np
import emd

x = np.loadtxt('highnoise.txt',usecols=0)
x = np.reshape(x,(1000,500))
x = np.average(x,axis=1)

y = np.loadtxt('highnoise.txt',usecols=1)
y = np.reshape(y,(1000,500))
y = np.average(y,axis=1)

data = np.sqrt(x**2+y**2)

imf = emd.sift.sift(data)
print(imf.shape)

IP, IF, IA = emd.spectra.frequency_transform(imf, 10, 'hilbert')

# Define frequency range (low_freq, high_freq, nsteps, spacing)
freq_range = (0.1, 10, 80, 'log')
f, hht = emd.spectra.hilberthuang(IF, IA, freq_range, sum_time=False)
fig1 = plt.figure(figsize=(12, 8))
emd.plotting.plot_imfs(imf,fig=fig1)
plt.tight_layout()

time_vect = np.linspace(0,100,1000)
fig2 = plt.figure(figsize=(10, 6))
ax = plt.axes()
emd.plotting.plot_hilberthuang(hht, time_vect, f,
                               time_lims=(2, 4), freq_lims=(0.1, 15),
                               fig=fig2, log_y=True,cmap='Spectral_r')


plt.show()