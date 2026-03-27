import time
import numpy as np

# Python list
start = time.time()
numbers = [i for i in range(1000000)]
squared = [i*i for i in numbers]
end = time.time()

print("Python list time:", end-start)


# NumPy
start = time.time()
arr = np.arange(1000000)
squared = arr ** 2
end = time.time()

print("NumPy array time:", end-start)