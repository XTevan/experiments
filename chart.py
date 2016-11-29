import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from scipy.stats import uniform

mu = 2
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-3, 6, 100)
plt.plot(x,mlab.normpdf(x,mu,sigma))

xn = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99),100)
plt.plot(xn,uniform.pdf(xn), 'r-', lw=5, alpha=0.6, label = 'uniform pdf')

plt.show()
