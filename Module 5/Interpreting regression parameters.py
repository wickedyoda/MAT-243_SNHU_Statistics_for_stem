import pandas as pd
import scipy.stats as st
df = pd.read_csv('http://data-analytics.zybooks.com/Reaction.csv') 
print(st.linregress(df['Drinks'],df['Reaction']))