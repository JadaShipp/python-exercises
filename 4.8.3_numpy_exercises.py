import numpy as np 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
mask = a % 2 == 0
a[mask].sum()