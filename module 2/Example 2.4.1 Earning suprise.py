import pandas as pd

# Create a DataFrame containing the eps data
earnings_surprise = pd.DataFrame([11.36, 7.89, 1.96, 0, -3.12, -9.52])
print(earnings_surprise.mean())
print(earnings_surprise.std())