#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/enron_email_dataset.pkl", "rb"))
features = ["salary", "bonus"]
del data_dict['TOTAL']

data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus)

# Finding the outliers (hughest salaries & bonuses)
for i in data_dict:
    # float() does not include NaN values
    bonus = float(data_dict[i]["bonus"])
    salary = float(data_dict[i]["salary"])
    if bonus >= 5000000 or salary >= 1000000:
        print(i, "bonus: ", data_dict[i]["bonus"], "salary: ", data_dict[i]["salary"])

# Finding the first largest value
max_salary_1 = 0
max_salary_1_key = ''

for data_element in data_dict:
    # print data_element[0]['salary']
    if data_dict[data_element]['salary'] != 'NaN' and data_dict[data_element]['salary'] > max_salary_1:
        max_salary_1 = data_dict[data_element]['salary']
        max_salary_1_key = data_element

print(max_salary_1_key)
print(max_salary_1)
print(data_dict[max_salary_1_key])

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
