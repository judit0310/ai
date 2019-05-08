import pandas as pd
import sklearn


flowers = pd.read_csv("data/iris.data", sep=",")
from sklearn.model_selection import train_test_split

features = ["sepal.length","sepal.width",
            "petal.length","petal.width"]
X = flowers[features]
Y=flowers["variety"]
X_train, X_test, Y_train, Y_test = \
    train_test_split(X,Y,random_state=0)
results = []
methods = []
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier().fit(X_train,Y_train)

print("DEcisiom tree :" + str(clf.score(X_test,Y_test)*100))
results.append(clf.score(X_test,Y_test)*100)
methods.append("Decision Tree")
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1,weights='distance')
knn.fit(X_train,Y_train)
print("KNN :" + str(knn.score(X_test,Y_test)*100))
results.append(knn.score(X_test,Y_test)*100)
methods.append("1NNW")
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,Y_train)
print("Naive Bayes :" + str(gnb.score(X_test,Y_test)*100))
results.append(gnb.score(X_test,Y_test)*100)
methods.append("NB")
print(results)

import matplotlib.pyplot as plt
plt.bar(methods,results)
plt.ylim(80, 100)
plt.show()