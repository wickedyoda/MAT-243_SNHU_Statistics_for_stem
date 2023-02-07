import pandas as pd
import statsmodels.formula.api as sms
import matplotlib.pyplot as plt

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

plt.figure(figsize = (20, 16))
plt.tight_layout()

plt.subplot(2, 2, 1)
plt.scatter(x = fat['triceps_skinfold_thickness_mm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['triceps_skinfold_thickness_mm'])
xmax = max(fat['triceps_skinfold_thickness_mm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_1$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_1$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 2)
plt.scatter(x = fat['midarm_circumference_cm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['midarm_circumference_cm'])
xmax = max(fat['midarm_circumference_cm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_2$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_2$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 3)
plt.scatter(x = fat['thigh_circumference_cm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['thigh_circumference_cm'])
xmax = max(fat['thigh_circumference_cm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_3$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_3$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 4)
plt.scatter(x = model.fittedvalues, y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(Y)
xmax = max(Y)
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('Fitted values', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Fitted values vs. residuals', fontsize = 24)
plt.show()