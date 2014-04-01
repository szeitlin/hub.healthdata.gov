import urllib
import string

#example query from open health website

url = 'http://hub.healthdata.gov/api/2/rest/dataset/b1dc5c2b-771a-4b54-ba03-94bc3d48f42d'
fileobj = urllib.urlopen(url)
j = fileobj.read()

#print j

#treats it as one big string; looks like a dict

#have to replace null, true, false values b/c they're not in quotes in the original file - Erin recommends using string_replace

filled = string.replace(j, ": null", ":None")
filled = string.replace(filled, ": true", ":True")
filled = string.replace(filled, ": false", ":False")

lyme_dict = eval(filled) #this converts it to a python dictionary

print lyme_dict.keys()





