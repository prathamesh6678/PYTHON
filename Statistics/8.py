import numpy as np

advertising_spend = [200, 250, 300, 400, 500]
daily_sales = [2200, 2450, 2750, 3200, 4000]

# Compute the correlation coefficient
correlation = np.corrcoef(advertising_spend, daily_sales)[0, 1]

print(f"Advertising Spend: {advertising_spend}")
print(f"Daily Sales: {daily_sales}")
print(f"Correlation Coefficient: {correlation}")