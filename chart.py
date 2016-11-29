import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from scipy.stats import uniform

def arran(x, y):
    for i in x:
        print(i)
        a = i * y
        print(" " + a)
        i = a
    return x

mu = 2
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-3, 6, 100)
y = mlab.normpdf(x,mu,sigma)
plt.plot(x,mlab.normpdf(x,mu,sigma))
plt.plot(x,arran(y,0.4),'r-')

xn = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99),100)
plt.plot(xn,uniform.pdf(xn), 'r-', lw=2, alpha=0.6, label = 'uniform pdf')

plt.show()
