import pandas as pd
print(pd.__version__)
import numpy as np

# From a Python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
print("steps array:", steps)
print("type:", type(steps))
print("dtype:", steps.dtype)
print("shape:", steps.shape)

# Zeros and ones
print("\nnp.zeros(5):", np.zeros(5))
print("np.ones(5):", np.ones(5))

# Range of numbers
print("np.arange(1, 8):", np.arange(1, 8))

# Evenly spaced
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

