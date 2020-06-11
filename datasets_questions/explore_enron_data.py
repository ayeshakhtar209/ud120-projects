#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/enron_email_dataset.pkl", "rb"))

# print(len(enron_data))

# for x in enron_data.values():
#     print(len(x))
#     break

################################################################

poi_count = 0

for x in enron_data:
    if enron_data[x]["poi"]:
        poi_count += 1

print(poi_count)

################################################################

# poi_list = np.loadtxt("../final_project/poi_names.txt", dtype="str", skiprows=2)
# print(len(poi_list))

################################################################

# if "PRENTICE JAMES" in enron_data:
#     stock_val = enron_data["PRENTICE JAMES"]["total_stock_value"]
#     print(stock_val)

################################################################

# if "COLWELL WESLEY" in enron_data:
#     poi_emails = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
#     print(poi_emails)

################################################################

# if "SKILLING JEFFREY K" in enron_data:
# #     exercised_stocks = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
# #     print(exercised_stocks)

################################################################

# mykeys = ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]
# tot_value = [(k, v["total_payments"]) for k, v in enron_data.items() if k in mykeys]
# print(tot_value)

################################################################

# salary_count = 0
# emails_count = 0
#
# for i in enron_data:
#     if enron_data[i]["salary"] != "NaN":
#         salary_count += 1
#
#     if enron_data[i]["email_address"] != "NaN":
#         emails_count += 1
#
# print(salary_count)
# print(emails_count)

################################################################

# no_sal = 0
#
# for i in enron_data:
#     if enron_data[i]["total_payments"] == "NaN":
#         no_sal += 1
#
# print(no_sal)
# print((no_sal/len(enron_data))*100)

################################################################

poi_nan_count = 0

for x in enron_data:
    if enron_data[x]["poi"] == True and enron_data[x]["total_payments"] == "NaN":
        poi_nan_count += 1

print((poi_nan_count+10 / poi_count+10) * 100)
print(poi_nan_count+10)
print(poi_count+10)