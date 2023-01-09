import pandas as pd

scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the first few lines of data
print(scores.head())

# Prints the mean for each exam
print(scores.mean())

# Prints the mean for Exam1 only
print(scores[['Exam1']].mean())

# Prints the means for Exam1 and Exam2
print(scores[['Exam1', 'Exam2']].mean())
