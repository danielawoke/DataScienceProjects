import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Loading of Dataset

data1 = pd.read_excel("2025-fall.xlsx")
data2 = pd.read_csv("2025-spr.csv")

# print(data1["How old are you?"].value_counts().max())


# DATA CLEANING

data2['How old are you?'] = data2['How old are you?'].apply(lambda x: int(x) if str(x).isdigit() else None )

# GRAPHING

jerk = "Not a jerk"

graph = data2[data2['How old are you?']>=20]["q5"].dropna()

print(graph.value_counts())

plt.xticks(np.arange(3), ["Not a jerk", "Mildly a jerk", "Strongly a jerk"])
plt.title("Aged 20 and above")
plt.xlabel("Age",fontsize=20, color='blue')
plt.ylabel("Quantity",fontsize=20, color='blue')

plt.hist(graph, bins = 20)

plt.show()


#HYPOTHESIS TESTING

Question = "q14"

sample1 = data2["How old are you?"].dropna()
sample2 = data2[data2[Question] == "Strongly a jerk"]["How old are you?"].dropna()

print(sample2)

print(sample1.mean())
print(stats.ttest_ind(sample1, sample2, alternative="greater"))