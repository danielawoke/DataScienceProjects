import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import seaborn as sns
import matplotlib.colors as colors

def gradeEncode(grade):
    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    else:
        return 1
def grade(grade):
    if grade>=.9:
        return "A"
    elif grade >=.8:
        return "B"
    elif grade >=.7:
        return "C"
    elif grade >=.6:
        return "D"
    else:
        return "F"
    
def passing(grade):
    if grade>=.7:
        return "Passing"
    else:
        return "Failing"
    


df = pd.read_csv('merged.csv')
df.dropna()
df["Grade"] = df["Total Score"]/df["Max Points"]
df = pd.get_dummies(df, columns=["I come to lecture:","I've had prior machine learning / data science experience","Which section are you in?","What year are you?","Did you do the readings?", "Did you leave the exam early?", "What grade do you think you got?","I wanted the extra credit but just put down random responses (you'll still get the extra credit if you say yes)"])
df = df.drop("Total Score", axis=1)
df = df.drop("Max Points", axis=1)

# df["Timestamp"] = df["Timestamp"].apply(lambda x : str(x))
# df.drop("Timestamp", axis=1)

# split = 100

# training = df[:split].copy(deep=True)
# testing = df[split+1:split+20].copy(deep=True)

# training = training.drop("Grade", axis=1)
# testing = testing.drop("Grade", axis=1)

# df["Passing"] = df["Grade"].apply(lambda x:"Passing" if x>=.7 else "Failing")

# print(training)
# training = df[]

df["Passing"] = df["Grade"].apply(lambda x: passing(x))

plt.xticks(np.arange(2), ["Failing", "Passing"])
plt.ylabel("Student count")
plt.hist(df["Passing"], bins = 3, histtype='stepfilled', alpha=0.7,color='skyblue', edgecolor='black')
plt.show()

# lin_reg = LinearRegression()
# clf = DecisionTreeClassifier()
# knn = GaussianNB()
# rf_classifier = MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam', max_iter=1000, random_state=42)

# knn.fit(training, df[:split]["Grade"].apply(lambda x:grade(x)))
# clf.fit(training, df[:split]["Grade"].apply(lambda x:grade(x)))
# rf_classifier.fit(training, df[:split]["Grade"].apply(lambda x:grade(x)))
# lin_reg.fit(training, df[:split]["Grade"])

# desTree = clf.predict(testing)
# KNN = knn.predict(testing)
# RAND = rf_classifier.predict(testing)
# pred = lin_reg.predict(testing)

# testing["Letter Grade"] = df[split+1:]["Grade"].apply(lambda x: passing(x))

# recall = 0

# for i in range(0,len(testing)):
#     # print(testing["Letter Grade"][121+i])
#     if(testing["Letter Grade"][i+split+1] == desTree[i]):
#         recall+=1

# print("DesTree: "+str(recall/len(testing)))


# recall = 0

# for i in range(0,len(testing)):
#     if(testing["Letter Grade"][i+split+1] == KNN[i]):
#         recall+=1

# print("DesTree: "+str(recall/len(testing)))


# recall = 0

# for i in range(0,len(testing)):
#     if(testing["Letter Grade"][i+split+1] == RAND[i]):
#         recall+=1

# print("DesTree: "+str(recall/len(testing)))




# print(mean_squared_error(df[split+1:split+20]["Grade"],pred))


#################

# des_tree = []

# # print(testing[0:1]["How many hours a day on average do you spend on sites with infinite scroll?"])
# data = testing[0:1].copy(deep=True)
# # print(testing.columns)
# for i in range(0,12):
#     lst = []
#     for j in range(0,72):
#         data["About how long, in hours, did you study for exam 1?"] = [j]
#         data["How many hours of sleep did you get the night before the exam?"] = [i]
#         frame = pd.DataFrame(data)
#         pred = rf_classifier.predict((frame))

#         lst.append(gradeEncode(pred[0]))
#     des_tree.append(lst)

# des_tree = np.array(des_tree)

# print(des_tree)

# hm = sns.heatmap(data=des_tree,
#                 annot=False)
  

# # Display the plot
# plt.show()
