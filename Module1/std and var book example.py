import pandas as pd

# Loads the ExamScores dataset
scores = [1, 2, 4, 5]

# Prints the standard deviation for each exam
print(scores())

# Prints the standard deviation for Exam1 only
print(scores[['Exam1']].std())

# Prints the variance for each exam
print(scores.var())

# Prints the variance for Exam1 only
print(scores[['Exam1']].var())