#!/usr/bin/python

"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/validation_poi.pkl", "rb"))

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

# Split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# it's all yours from here forward!
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
acc = accuracy_score(y_test, pred)
# print(len(X_test))

# pred = [0.] * 29
# accuracy = accuracy_score(y_test, pred)
# print(accuracy)

#print(confusion_matrix(y_test, pred))

count = 0
for p, y in zip(pred, y_test):
    if p == y == 1:
        count += 1

print(count)

print(precision_score(y_test, pred))
print(recall_score(y_test, pred))
