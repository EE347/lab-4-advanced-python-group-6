import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

for i in range(1,7):
    for j in range(1,7):
        x[i][j] = 0

print('After:') 
print(x)