import matplotlib.pyplot as plt
import os
import numpy as np 

n=5
x = np.arange(n)
y = np.sin(np.linspace(-3,3,n))
xlabels = ['Ticklabel %i' % i for i in range(9)]

fig, ax = plt.subplots()

ax.plot(x,y, 'o-')
ax.set_xticks(x)
ax.set_xticklabels(xlabels, rotation=40)

plt.show()