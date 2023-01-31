#Import the necessary libraries:
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#Load the data into a Pandas DataFrame:
data = pd.read_csv("your_data.csv")

#Split the data into a training set and a test set:
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.iloc[:,-1], test_size=0.2, random_state=0)

#Fit the linear regression model on the training data:
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Make predictions using the test data:
y_pred = regressor.predict(X_test)

#Evaluate the model by computing the mean squared error:
mse = mean_squared_error(y_test, y_pred)
#Optionally, you can print the coefficients and the intercept of the model:

print("Coefficients: ", regressor.coef_)
print("Intercept: ", regressor.intercept_)