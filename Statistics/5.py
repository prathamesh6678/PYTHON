import numpy as np
from scipy import stats

numbers = [12, 15, 12, 18, 19, 12, 20, 22, 19, 19, 24, 24, 24, 26, 28]

# Compute Mean
mean_value = np.mean(numbers)

# Compute Median
median_value = np.median(numbers)

# Compute Mode
try:
    mode_result = stats.mode(numbers, keepdims=True)
    mode_value = mode_result.mode[0]
except TypeError:
    mode_result = stats.mode(numbers)
    mode_value = mode_result.mode[0]

print(f"Given numbers: {numbers}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
