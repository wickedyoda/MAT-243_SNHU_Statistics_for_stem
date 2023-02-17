## Question 1: 

Data: The following is an accessible version of the Python script output for OLS Regression. In the normal output, the items are arranged in two columns.

Here, items are listed in one column for easier use. Each item has a label. For
example, the label “Model” comes before the item “OLS”. Items follow the same
order as the normal Python script output.

## OLS Regression Results

Dependent Variable: Quality

Model: OLS

Method: Least Squares

Date: Sun, 18 Aug 2019

Time: 11:39:31

No. Observations: 18

Df Residuals: 15

Df Model: 2

Covariance Type: nonrubust

R-squared: 0.978

Adj. R-squared: 0.975

F-statistic: 332.2

Prob (F-statistc): 3.80 e -13

Log-Likelihood: -21.142

AIC: 48.28

BIC: 50.95

|     |  Coef  |  Std
   err  |  T  |  P>|t|  |  [0.025  |  0.975]  |
|  Intercept  |  0.5382  |  0.473  |  1.137  |  0.273  |  -0.471  |  1.547  |
|  Speed  |  -1.9046  |  0.176  |  -10.834  |  0.000  |  -2.279  |  -1.530  |

| Angle | 4.0280 | 0.178 | 22.574 | 0.000 | 3.648 | 4.408 |
| ----- | ------ | ----- | ------ | ----- | ----- | ----- |

Omnibus: 4.358

Prob(Omnibus): 0.113

Skew: 0.082

Kurtosis: 1.637

Durbin-Watson: 2.121

Jarque-Bera (JB): 1.414

Prob(JB): 0.493

Cond. No: 14.4


Question: 

The statsmodels ols() method is used on a cars dataset to fit a multiple regression model using *Quality* as the response variable. *Speed and Angle* are used as predictor variables. The general form of this model is:

![Y-hat equals beta sub zero plus beta sub one times speed plus beta sub two times angle. Speed and angle are variables.](https://learn.snhu.edu/content/enforced/1230325-MAT-243-J3996-OL-TRAD-UG.23EW3/course_documents/MAT%20243%20Module%20Quiz%20Images/Module%20Seven%20Quiz%20Image%202.png?_&d2lSessionVal=3OM4YJxPt5BLTG77cE2WRsEjn "Y-hat equals beta sub zero plus beta sub one times speed plus beta sub two times angle. Speed and angle are variables.")

If the level of significance, alpha, is 0.05, based on the output shown, what is the correct interpretation of the overall F-test? (Hint: Prob (F-statistic) is the P-value). Select one.


## Question 2:

Consider the following multiple regression model. What are the correct null and alternative hypotheses to test whether the variable *x~2~* is significant? Select one.


Question 2 options:| [ ]  

| Null Hypothesis ![The null hypothesis states that beta sub zero does not equal zero.](https://learn.snhu.edu/content/enforced/1230325-MAT-243-J3996-OL-TRAD-UG.23EW3/course_documents/MAT%20243%20Module%20Quiz%20Images/Module%20Seven%20Quiz%20Image%2016.png?_&d2lSessionVal=3OM4YJxPt5BLTG77cE2WRsEjn "The null hypothesis states that beta sub zero does not equal zero.")`<br/>`Alternative Hypothesis![The alternative hypothesis states that beta sub zero equals zero.](https://learn.snhu.edu/content/enforced/1230325-MAT-243-J3996-OL-TRAD-UG.23EW3/course_documents/MAT%20243%20Module%20Quiz%20Images/Module%20Seven%20Quiz%20Image%2017.png?_&d2lSessionVal=3OM4YJxPt5BLTG77cE2WRsEjn "The alternative hypothesis states that beta sub zero equals zero.") |

| [ ]  | Null Hypothesis
Alternative Hypothesis   |
| [ ]  | Null Hypothesis
Alternative Hypothesis     |
| [ ]  | Null Hypothesis 

| Alternative Hypothesis |  |  |  |  |  |  |  |
| ---------------------- | - | - | - | - | - | - | - |
| <br />                 |  |  |  |  |  |  |  |


## Question 3:

A multiple regression model is ![Y-hat equals 8.114 plus 2.005 times x sub one plus 0.774 times x sub two.](https://learn.snhu.edu/content/enforced/1230325-MAT-243-J3996-OL-TRAD-UG.23EW3/course_documents/MAT%20243%20Module%20Quiz%20Images/Module%20Seven%20Quiz%20Image%201.png?_&d2lSessionVal=3OM4YJxPt5BLTG77cE2WRsEjn "Y-hat equals 8.114 plus 2.005 times x sub one plus 0.774 times x sub two.")
Which of the following values is the estimate for the intercept parameter? Select one.

Question 3 options:| [ ]  | 1.000 |
| ------- | ------- |
| [ ]  | 8.114 |
| [ ]  | 0.774 |
| [ ]  | 2.005 |


## Question 4:

Data: 

Description: The following is an accessible version of the Python script output for OLS Regression. In the normal output, the items are arranged in two columns. Here, items are listed in one column for easier use. Each item has a label. For example, the label “Model” comes before the item “OLS”. Items follow the same order as the normal Python script output.

##### OLS Regression Results

Dependent Variable:
Exam4

Model: OLS

Method: Least
Squares

Date: Sun, 18 Aug
2019

Time: 10:59:12

No. Observations: 50

Df Residuals: 46

Df Model: 3

Covariance Type:
nonrubust

R-squared: 0.178

Adj. R-squared:
0.125

F-statistic: 3.329

Prob (F-statistc):
0.0276

Log-Likelihood:
-169.85

AIC: 347.7

BIC: 355.4

|     |  **Coef**  |  **Std err**  |  **T**  |  **P>|t|**  |  **[0.025**  |  **0.975]**  |
|  **Intercept**  |  46.2612  |  10.969  |  4.217  |  0.000  |  24.181  |  68.341  |
|  **Exam1**  |  0.1742  |  0.120  |  1.453  |  0.153  |  -0.067  |  0.416  |
|  **Exam2**  |  0.1462  |  0.078  |  1.873  |  0.067  |  -0.011  |  0.303  |

| **Exam3** | 0.0575 | 0.053 | 1.085 | 0.284 | -0.049 | 0.164 |
| --------------- | ------ | ----- | ----- | ----- | ------ | ----- |

Omnibus: 0.886

Prob(Omnibus): 0.642

Skew: 0.290

Kurtosis: 2.868

Durbin-Watson: 1.530

Jarque-Bera (JB):
0.738

Prob(JB): 0.691

Cond. No: 1.41 e
plus 03

#### Question:

The statsmodels ols() method is used on an exam scores dataset to fit a multiple regression model using *Exam4* as the response variable.  *Exam1* ,  *Exam2* , and *Exam3* are used as predictor variables. The general form of this model is:

Y=B0+B1*Exam*1+B2*Exam*2+B3*Exam*3

If the level of significance, alpha, is 0.10, based on the output shown, is *Exam1* statistically significant in the multiple regression model shown above? Select one.

## Question 5:

What is the purpose of performing the overall F-test? Select one.

Question 5 options:| [ ]  | It is used to estimate the sum of squared residuals.                                                                  |
| [ ]  | It is used to test whether at least one of the predictor variables is significant in `<br/>`a regression model.              |
| [ ]  | It is used to test if a specific predictor variable is significant in a regression `<br/>`model.                             |
| [ ]  | It is used to test two regression models to test whether additional predictor `<br/>`variables should be added in the model. |
