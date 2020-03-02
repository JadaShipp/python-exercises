import numpy as np 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
mask = a < 0
mask.sum()

# 2. How many positive numbers are there?
mask = a > 0
a[mask].sum()

# 3. How many even positive numbers are there?
a = a[a > 0]
a = a[a % 2 == 0]
a.size

# 4. If you were to add 3 to each data point, 
# how many positive numbers would there be?

a2 = a + 3
mask = a2 >0
mask.sum

