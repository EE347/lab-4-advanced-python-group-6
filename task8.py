import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)

sin = np.load("task7_sin.npy")
cos = np.load("task7_cos.npy")

plt.plot(x, sin, color='blue', label='sin(x)')
plt.plot(x, cos, color='orange', label='cos(x)')
plt.legend(loc='lower left')
plt.show()