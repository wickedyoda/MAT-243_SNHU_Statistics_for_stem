Data from project 1:

    Data from step 1:

|   | game_id      | year_id | fran_id | pts | opp_pts | elo_n     | opp_elo_n | game_location | game_result |
| - | ------------ | ------- | ------- | --- | ------- | --------- | --------- | ------------- | ----------- |
| 0 | 199511030CHI | 1996    | Bulls   | 105 | 91      | 1598.2924 | 1531.7449 | H             | W           |
| 1 | 199511040CHI | 1996    | Bulls   | 107 | 85      | 1604.3940 | 1458.6415 | H             | W           |
| 2 | 199511070CHI | 1996    | Bulls   | 117 | 108     | 1605.7983 | 1310.9349 | H             | W           |
| 3 | 199511090CLE | 1996    | Bulls   | 106 | 88      | 1618.8701 | 1452.8268 | A             | W           |
| 4 | 199511110CHI | 1996    | Bulls   | 110 | 106     | 1621.1591 | 1490.2861 | H             | W           |

printed only the first five observations...
Number of rows in the dataset = 246

    Data from step 2:

|   | game_id      | year_id | fran_id | pts | opp_pts | elo_n     | opp_elo_n | game_location | game_result |
| - | ------------ | ------- | ------- | --- | ------- | --------- | --------- | ------------- | ----------- |
| 0 | 201210300MIA | 2013    | Heat    | 120 | 107     | 1666.3193 | 1586.1121 | H             | W           |
| 1 | 201211020NYK | 2013    | Heat    | 84  | 104     | 1647.6675 | 1548.2699 | A             | L           |
| 2 | 201211030MIA | 2013    | Heat    | 119 | 116     | 1650.0934 | 1554.4674 | H             | W           |
| 3 | 201211050MIA | 2013    | Heat    | 124 | 99      | 1656.5652 | 1504.0280 | H             | W           |
| 4 | 201211070MIA | 2013    | Heat    | 103 | 73      | 1659.7239 | 1361.5804 | H             | W           |

printed only the first five observations...
Number of rows in the dataset = 246

    Data from step 3:
	Mean Relative Skill of your team in the years 2013 to 2015 = 1617.48
	Hypothesis Test for the Population Mean
	Test Statistic = 43.55
	P-value = 0.0

Data from step 4:

    Mean Points Scored by your team in the years 2013 to 2015 = 99.92
	Hypothesis Test for the Population Mean
	Test Statistic = -8.7
	P-value = 0.0

Data from step 5:

    Proportion of games won by your team when scoring more than 102 points in the years 2013 to 2015 = 0.8922
	Hypothesis Test for the Population Proportion
	Test Statistic = -0.26
	P-value = 0.7917

Data from step 6:

    Mean Relative Skill of the assigned team in the years 1996 to 1998 = 1739.8
	Mean Relative Skill of your team in the years 2013 to 2015  = 1617.48
	Hypothesis Test for the Difference Between Two Population Means
	Test Statistic = 17.07
	P-value = 0.0

Requirements:

    1. Each paragrah must have a minimal of 3 sentences

Ansewer the following:

You created a multiple regression model with the total number of wins as the response variable, with average points scored, average relative skill, average points differential, and average relative skill differential as predictor variables.

See Step 6 in the Python script to answer the following questions:

•	In general, how is a multiple linear regression model used to predict the response variable using predictor variables? 
•	What is the equation for your model? 
•	What are the results of the overall F-test? Summarize all important steps of this hypothesis test. This includes:
		a.	Null Hypothesis (statistical notation and its description in words)
		b.	Alternative Hypothesis (statistical notation and its description in words)
		c.	Level of Significance 
		d.	Report the test statistic and the P-value in a formatted table as shown below:
		e.	Conclusion of the hypothesis test and its interpretation based on the P-value 
•	Based on the results of the overall F-test, is at least one of the predictors statistically significant in predicting the number of wins in the season? 
•	What are the results of individual t-tests for the parameters of each predictor variable?  Is each of the predictor variables statistically significant based on its P-value? Use a 1% level of significance.
•	Report and interpret the coefficient of determination.
•	What is the predicted total number of wins in a regular season for a team that is averaging 75 points per game with a relative skill level of 1350, average point differential of -5 and average relative skill differential of -30?
•	What is the predicted total number of wins in a regular season for a team that is averaging 100 points per game with a relative skill level of 1600, average point differential of +5 and average relative skill differential of +95? 


