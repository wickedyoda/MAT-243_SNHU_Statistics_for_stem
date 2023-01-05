import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the minimum score for each exam
print(scores.min())

# Prints the minimum score for Exam1 only
print(scores[['Exam1']].min())

# Prints the maximum score for each exam
print(scores.max())

# Prints the maximum score for Exam1 only
print(scores[['Exam1']].max())