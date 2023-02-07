import pandas as pd
import statsmodels.formula.api as sms

cars = pd.read_csv('http://data-analytics.zybooks.com/Cars.csv')

# Response variable
Y = cars['Quality']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ Speed + Angle', cars).fit()

print(model.fittedvalues)