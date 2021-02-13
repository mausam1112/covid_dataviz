# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:11:03 2020

@author: Admin
"""

with open('data_history_oct_2.txt') as file:
    data = file.readlines()
    # here data is of list data type. data[0] gives the string dtype
    # data[0][3:-2] slices the string
    data = data[0][3:-2]
    data = data.replace("},", "}\n")

    
with open('data_history_oct_2_processed.txt','w') as file1:
    file1.write(data)

with open('data_history_oct_2_processed.txt') as file:
    data = file.readlines()

import json

temp_dict = {}
temp_dict['date'] = []
temp_dict['totalCases'] = []
temp_dict['newCases'] = []
temp_dict['totalRecoveries'] = []
temp_dict['newRecoveries'] = []
temp_dict['totalDeaths'] = []
temp_dict['newDeaths'] = []

#converting string into dictionary
for i in range(len(data)):
    data_dict = json.loads(data[i])
    temp_dict['date'].append(data_dict['date'])
    temp_dict['totalCases'].append(data_dict['totalCases'])
    temp_dict['newCases'].append(data_dict['newCases'])
    temp_dict['totalRecoveries'].append(data_dict['totalRecoveries'])
    temp_dict['newRecoveries'].append(data_dict['newRecoveries'])
    temp_dict['totalDeaths'].append(data_dict['totalDeaths'])
    temp_dict['newDeaths'].append(data_dict['newDeaths'])


with open('data_history_oct_2.json','w') as outfile:
    json.dump(temp_dict, outfile)
    

    