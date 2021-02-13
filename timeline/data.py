# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:45:02 2020

@author: Admin
"""

#import requests
#url = "https://data.nepalcorona.info/api/v1/covid"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))



'''history'''
import requests
url = "https://data.nepalcorona.info/api/v1/covid/timeline"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))
print(response.text)

#for other datas

#import requests
#url = "https://data.nepalcorona.info/api/v1/covid"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))


'''summary count'''

#import requests
#url = "https://data.nepalcorona.info/api/v1/covid/summary"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))


'''Districts List'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/districts"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))

'''District Details'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/districts/:districtId"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))


'''municipality list'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/municipals"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))



outfile = open('data_history_oct_2.txt', 'w')
outfile.write(response.text)
