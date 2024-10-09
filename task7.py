import numpy as np

x = np.linspace(0, 10, 101)

sin = np.sin(x)
cos = np.cos(x)

np.save("task7_sin", sin)
np.save("task7_cos", cos)

print(x)