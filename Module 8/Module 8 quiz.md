Question1:

A biologist is studying the composition of birds on a lake and counts 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons. From previous studies performed around the same time of the year, she expects 50% of the birds to be ducks, 23% to be geese, 12% to be cranes, 10% to be swans, and 5% to be herons. What are the correct null and alternative hypotheses for performing a chi-square goodness of fit test? Select one.

Question 1 options: 

| [ ]  | Null Hypothesis *H~0~* : The distribution of birds observed does not follow the distribution from previous studies.`<br/>`Alternative Hypothesis  *H~1~* : The distribution of birds observed follows the distribution from previous studies. |

| [ ]  | Null Hypothesis *H~0~* : The distribution of birds observed follows the distribution from previous studies.`<br/>`Alternative Hypothesis  *H~1~* : The distribution of birds observed does not follow the distribution from previous studies. |
| [ ]  | Null Hypothesis *H~0~* : The distribution of birds observed follows the Student’s t-distribution.`<br/>`Alternative Hypothesis  *H~1~* : The distribution of birds observed does not follow the Student’s t-distribution.                   |
| [ ]  | Null Hypothesis *H~0~* : The distribution of birds observed follows the Normal distribution.`<br/>`Alternative Hypothesis  *H~1~* : The distribution of birds observed does not follow the Normal distribution.           |

Answer: 

The correct null and alternative hypotheses for performing a chi-square goodness of fit test in this scenario are:

Null Hypothesis  *H~0~* : The distribution of birds observed follows the distribution from previous studies.
Alternative Hypothesis  *H~1~* : The distribution of birds observed does not follow the distribution from previous studies.

Therefore, the correct option is:
[ ] | Null Hypothesis *H~0~* : The distribution of birds observed does not follow the distribution from previous studies.`<br/>`Alternative Hypothesis  *H~1~* : The distribution of birds observed follows the distribution from previous studies. |

Question 2: 


What is the use of the chi-square goodness of fit test? Select one.

Question 2 options:| 

| [ ] | To test the difference in three or more population means                             |
| --- | ------------------------------------------------------------------------------------ |
| [ ] | To test how close the distribution of a population is to an expected distribution    |
| [ ] | To test how close the distribution of a population is to a Student’s t-distribution |
| [ ] | To test how close the distribution of a population is to a Normal distribution       |

Answer: 

The use of the chi-square goodness of fit test is to test how close the distribution of a population is to an expected distribution. Therefore, the correct option is:

| [X] | To test how close the distribution of a population is to an expected distribution |


Question 3:


A university conducted a survey of its recent graduates. The university wanted to measure the quality of a new Engineering course. A survey was conducted during the first offering of the course to evaluate its overall quality. The results of the survey are shown below:

Needs Improvement: 55%
Meets Expectations: 30%
Excellent: 15%

The university made improvements to the course earlier this year. Then it conducted another survey to evaluate how these improvements worked. A total of 500 students were surveyed. Their results are shown below:

Needs Improvement: 175 students
Meets Expectations: 225 students
Excellent: 100 students

You want to perform a chi-square test for goodness of fit, to see if students’ views have changed about the course. Which of the following Python scripts prints the P-value and test statistic for the chi-square test? Select one.

Question 3 options:

| [ ]  | from scipy.stats import chisquare `<br/>`statistic, pvalue = chisquare([275,150,75], f_exp=[175,225,100])`<br/>`print(statistic)`<br/>`print(pvalue)       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [ ]  | from scipy.stats import chisquare `<br/>`statistic, pvalue = chisquare([175,225,100], f_exp=[275,150,75])`<br/>`print(statistic)`<br/>`print(pvalue)       |
| [ ]  | from scipy.stats import chisquare `<br/>`statistic, pvalue = goodness_of_fit([275,150,75], f_exp=[175,225,100])`<br/>`print(statistic)`<br/>`print(pvalue) |
| [ ]  | from scipy.stats import chisquare `<br/>`statistic, pvalue = goodness_of_fit([175,225,100], f_exp=[275,150,75])`<br/>`print(statistic)`<br/>`print(pvalue) 

Answer:


The correct Python script that prints the P-value and test statistic for the chi-square test is:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">scss</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-scss">from scipy.stats import chisquare
observed = [175, 225, 100]
expected = [275, 150, 75]
statistic, pvalue = chisquare(observed, f_exp=expected)
print(statistic)
print(pvalue)
</code></div></div></pre>

Therefore, the answer is:

| [X] | from scipy.stats import chisquare `<br/>`observed = [175, 225, 100]`<br/>`expected = [275, 150, 75]`<br/>`statistic, pvalue = chisquare(observed, f_exp=expected)`<br/>`print(statistic)`<br/>`print(pvalue) |

Question 4: 


Which of the following Python methods is used to perform chi-square goodness of fit tests? Select one.

Question 4 options:

| [ ] | f_oneway from scipy.stats submodule  |
| --- | ------------------------------------ |
| [ ] | tukeyhsd from scipy.stats submodule  |
| [ ] | chisquare from scipy.stats submodule |
| [ ] | anova_lm from scipy.stats submodule  |
|     |                                      |
|     |                                      |

Answer:

The correct answer is:

| [ ] | f_oneway from scipy.stats submodule  |
| --- | ------------------------------------ |
| [ ] | tukeyhsd from scipy.stats submodule  |
| [x] | chisquare from scipy.stats submodule |
| [ ] | anova_lm from scipy.stats submodule  |


Question 5:

A biologist is studying the composition of birds on a lake and counts 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons. From previous studies performed around the same time of the year, she expects 50% of the birds to be ducks, 23% to be geese, 12% to be cranes, 10% to be swans, and 5% to be herons. What are the expected and observed counts? Select one.

Question 5 options:

| [ ]  | Expected = 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons `<br/>`Observed = 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons |
| [ ]  | Expected = 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons `<br/>`Observed = 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons |
| [ ]  | Expected = 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons `<br/>`Observed = 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons |
| [ ]  | Expected = 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons `<br/>`Observed = 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons 

Answer: 

The biologist expects 50%, 23%, 12%, 10%, and 5% of the birds to be ducks, geese, cranes, swans, and herons, respectively. Since she counted 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons, the expected counts are:

* Ducks: 50% of the total count = 0.50 x 110 = 55
* Geese: 23% of the total count = 0.23 x 110 = 25.3 (rounded to 25)
* Cranes: 12% of the total count = 0.12 x 110 = 13.2 (rounded to 13)
* Swans: 10% of the total count = 0.10 x 110 = 11
* Herons: 5% of the total count = 0.05 x 110 = 5.5 (rounded to 6)

Therefore, the expected counts are 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons.

The observed counts are given as 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons.

Therefore, the answer is:

Expected = 55 ducks, 25 geese, 13 cranes, 11 swans, and 6 herons
Observed = 61 ducks, 17 geese, 11 cranes, 15 swans, and 6 herons
