import numpy as np

def square(x):
    return x*x

def coulomb(r):
    assert type(r) in [float, int], "You passed an invalid argument"
    try:
        return 1 / abs(r)
    except ZeroDivisionError:
        print('Division by zero. Returned zero potential.')
        return 0.0      

def CentralDifference(f, x, h):
    # f(x + h) - f(x - h)
    # -------------------    \approx f'(x)
    #         2*h
    return (f(x+h) - f(x-h))/(2*h)

hs = []
vals = []
for i in range(2, 8):
    h = 10**(-i)
    hs.append(h) 
    vals.append(abs(CentralDifference(np.sin, 0.0, h) - 1.0)))

import matplotlib.pyplot as plt

plt.loglog(hs, vals)
plt.imshow

