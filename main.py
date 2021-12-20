import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate.odepack import odeint

import series.iterators as iterators
from series.iterators import *

if __name__ == '__main__':
    xlist = np.linspace(-1.1, 1.1)
    ylist = iterators.calcualte_up_x(xlist, 10, 10)

    plt.figure(num=0, dpi=10)
    plt.plot(xlist, ylist)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
