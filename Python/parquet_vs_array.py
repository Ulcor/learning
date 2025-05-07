from sklearn.datasets import make_friedman1
import pandas as pd

X, y = make_friedman1(random_state=1)

df = pd.DataFrame(X)
df.to_parquet('df.parquet')

pd.read_parquet('df.parquet')