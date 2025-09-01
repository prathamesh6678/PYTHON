import matplotlib.pyplot as plt

survey_scores = [7, 8, 5, 9, 6, 7, 8, 9, 10, 4, 7, 6, 9, 8, 7]

plt.hist(survey_scores, bins=range(1, 12), edgecolor='black', rwidth=0.8)
plt.title('Customer Satisfaction Survey Score Distribution')
plt.xlabel('Survey Scores (1-10)')
plt.ylabel('Frequency')
plt.xticks(range(1, 11))
plt.show()

print(f"Survey Scores: {survey_scores}")