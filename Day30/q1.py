import scipy as sp
import numpy as np
import scipy.optimize as spo

X = np.array([2,3,5,7,9])

Y = np.array([4,5,7,10,15])

fxf = lambda m,x,c: m*x+c

popt,pcov = spo.curve_fit(fxf,X,Y)

print(popt)

fxf(popt[0],10,popt[1])

vfxf = sp.vectorize(fxf)
cy = vfxf(popt[0],X,popt[1])


import matplotlib.pyplot as plt

plt.plot(X,Y,'r:o',label='observed')
plt.plot(X,cy,'b-v',label='calculated')

plt.legend(loc='best')
plt.show()
