# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:45:02 2020

@author: Admin
"""


'''history'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/covid/timeline"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text)


'''details'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/covid"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text)


'''summary count'''

#import requests
#url = "https://data.nepalcorona.info/api/v1/covid/summary"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)


'''Districts List'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/districts"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text)


'''District Details'''
import requests
url = "https://data.nepalcorona.info/api/v1/districts/:districtId"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)


'''municipality list'''
#import requests
#url = "https://data.nepalcorona.info/api/v1/municipals"
#payload = {}
#headers= {}
#response = requests.request("GET", url, headers=headers, data = payload)



outfile = open('summary_sep_17.txt', 'w')
outfile.write(response.text)
