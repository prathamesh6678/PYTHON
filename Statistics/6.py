import numpy as np

list_x = [10, 20, 30, 40, 50]
list_y = [15, 25, 35, 45, 60]

# Compute Covariance
covariance = np.cov(list_x, list_y)[0, 1]

# Compute Correlation Coefficient
correlation_coefficient = np.corrcoef(list_x, list_y)[0, 1]

print(f"List X: {list_x}")
print(f"List Y: {list_y}")
print(f"Covariance: {covariance}")
print(f"Correlation Coefficient: {correlation_coefficient}")