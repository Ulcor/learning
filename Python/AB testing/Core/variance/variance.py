import numpy as np
import pandas as pd

data = [2, 4, 4, 4, 5, 5, 7, 9, 9]

# Dispersion
population_variance = np.var(data)      # no adjustment on n-1 (general)
sample_variance = np.var(data, ddof=1)   # with adjustment on n-1 (unbiased estimator)

print(f"Population Variance: {population_variance:.2f}")
print(f"Sample Variance: {sample_variance:.2f}")

# Альтернативно с pandas
df = pd.DataFrame({'values': data})
print(f"Pandas Sample Variance: {df['values'].var():.2f}")

# variance = дисперсия
