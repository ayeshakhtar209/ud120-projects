#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import numpy
import matplotlib.pyplot as plt
import sys
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for
    # drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color=colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


# load in the dict of dicts containing all the data on each person in the data set
data_dict = pickle.load(open("../final_project/enron_email_dataset.pkl", "rb"))
# there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

# the input features we want to use
# can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi = "poi"

features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)

# feature scaling on salary and exercised stock optons
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(finance_features)

#######################################################
salary = []
stocks = []
for key, val in data_dict.items():
    if val["salary"] != 'NaN':
        salary.append(val["salary"])

for key, val in data_dict.items():
    if val["exercised_stock_options"] != 'NaN':
        stocks.append(val["exercised_stock_options"])

salary.sort()
min_sal = salary[0]
max_sal = salary[-1]

stocks.sort()
min_stock = stocks[0]
max_stock = stocks[-1]

# scaled_sal = (200000 - min_sal) / float(max_sal - min_sal)
# scaled_stock = (1000000 - min_stock) / float(max_stock - min_stock)
#
# print(scaled_sal) 0.17962406631010072
# print(scaled_stock) 0.029020588934683227

scaled_sal = scaler.fit_transform([[min_sal], [200000.], [max_sal]])
scaled_st = scaler.fit_transform([[min_stock], [1000000.], [max_stock]])

print(scaled_sal)
print(scaled_st)
########################################################

# in the "clustering with 3 features" part of the mini-project,
# you'll want to change this line to 
# for f1, f2, _ in finance_features:
# (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter(f1, f2)
plt.show()

# cluster here; create predictions of the cluster labels
# for the data and store them to a list called pred

pred = KMeans(n_clusters=2).fit_predict(scaled_data)

# rename the "name" parameter when you change the number of features
# so that the figure gets saved to a different file
try:
    Draw(pred, scaled_data, poi, mark_poi=False, name="feature-scaling.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")
