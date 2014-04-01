import urllib2
import urllib
import json
import pprint
import pandas

import numpy
import string

#read data from a CSV file using the CKAN API

#dataset details
#dataset_dict = {
#    'name' : 'my_dataset_name',
#    'notes': 'A long decription of the dataset',
#}

#example query from open health website

#use json dictionary that will be posted
#data_string = urllib.quote(json.dumps{dataset_dict}) #not sure what goes in here

#HTTP request to get list of datasets, should return a list of strings?
request = urllib.urlopen('http://hub.healthdata.gov/api/3/action/package_list')
j = request.read()

#CKAN responds with another json
response_dict = json.loads(j)

#assert response.code == 200 #somewhere they explained what this means, I think it's success/fail?

#check if it worked:
#assert response_dict['success'] is True
#result = response_dict['result']
pprint.pprint(response_dict)

#have to replace null, true, false values b/c they're not in quotes in the original file - Erin recommends using string_replace

#filled = string.replace(j, ": null", ":None")
#filled = string.replace(filled, ": true", ":True")
#filled = string.replace(filled, ": false", ":False")

#lyme_dict = eval(filled) #this converts it to a python dictionary

#print lyme_dict.keys()

#would like to get a list of packages satisfying certain criteria, i.e. minimum # rows
#ckan.logic.action.get.package_search(context, data_dict)
#Solr search parameters includes an option for rows (int)

#e.g. http://hub.healthdata.gov/api/e/action/package_search?q=rows=50

#should return a dictionary with keys including count(int), i.e. the total number of results




