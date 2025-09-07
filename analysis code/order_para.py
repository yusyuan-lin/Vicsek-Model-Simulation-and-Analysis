import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['science', 'notebook'])

x =np.loadtxt('simulation_data.txt',usecols=0)
x = np.reshape(x,(200,500))

theta =np.loadtxt('simulation_data.txt',usecols=4)
theta = np.reshape(theta,(200,500))

v0 = 1
vn = v0*np.exp(1j*theta)

def order_parameter(N,v0,v,sh):
    va = np.zeros(sh)
    for i in range(sh):
        va[i] = (1/(N*v0))*np.abs(np.sum(v[i]))
    return va

op = order_parameter(500,v0,vn,200)

#plt.plot(vn[:,100])
plt.plot(op,'o')
plt.xlabel('time')
plt.ylabel('va')
plt.title('order parameter')
plt.show()
