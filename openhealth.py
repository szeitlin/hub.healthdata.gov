import urllib
import simplejson as json
import pandas
import numpy

#example query from open health website

url = 'http://hub.healthdata.gov/api/action/datastore_search?limit=5&q=title:jones'
fileobj = urllib.urlopen(url)
j = fileobj.read()

print "original file looks like this: " + j

#parse into something readable

#cleanup = pandas.read_csv(fileobj, sep='\s*')

#print cleanup

def parse_instructions():
    """
    dict --> list of str (?)
    goal being to identify query strings for use in R
    
parse_instructions({"help": "Search a datastore table.\n\n    
The datastore_search action allows a user to search data in a resource.\n\n    
:param resource_id: id or alias of the resource to be searched against.\n    
:type resource_id: string\n    
:param filters: matching conditions to select, e.g {\"key1\": \"a\", \"key2\": \"b\"}\n    
:type filters: dictionary\n    
:param q: full text query\n    
:type q: string\n    
:param plain: treat as plain text query (default: true)\n    
:type plain: bool\n    
:param language: language of the full text query (default: english)\n    
:type language: string\n    
:param limit: maximum number of rows to return (default: 100)\n    
:type limit: int\n    
:param offset: offset this number of rows\n    
:type offset: int\n    
:param fields: fields to return (default: all fields in original order)\n    
:type fields: list or comma separated string\n    
:param sort: comma separated field names with ordering\n                 e.g.
: \"fieldname1, fieldname2 desc\"\n    
:type sort: string\n\n    
Setting the ``plain`` flag to false enables the entire PostgreSQL `full text search query language`_.\n\n    

A listing of all available resources can be found at the alias ``_table_metadata``.\n\n    .. _
full text search query language: http://www.postgresql.org/docs/9.1/static/datatype-textsearch.html#DATATYPE-TSQUERY\n\n    

**Results:**\n\n    
The result of this action is a dict with the following keys:\n\n    
:rtype: A dictionary with the following keys\n    
:param fields: fields/columns and their extra metadata\n    
:type fields: list of dictionaries\n    
:param offset: query offset value\n    
:type offset: int\n    
:param limit: query limit value\n    
:type limit: int\n    
:param filters: query filters\n    
:type filters: list of dictionaries\n    
:param total: number of total matching records\n    
:type total: int\n    
:param records: list of matching results\n    
:type records: list of dictionaries\n\n    
", "success": false, "error": {"__type": "Validation Error", "resource_id": "Missing value"}})

   """

#rows = ( line.split('\t') for line in j )

#p = re.compile('\A:') #\A matches only at the beginning of the string
#for word in j:
#    line = re.sub(p, ",", word) #rstrip removing trailing characters ("characters on the right")
#print line
#r = q.sub(p.match(j), "")
#print r
#json_obj = json.load(fileobj)
#print "the json obj looks like this: " + json_obj


#print newstring_as_dict #this didn't work - value error

#try this instead, assuming it is a json with trailing text?

#decoder = json.JSONDecoder()
#def get_decoded_and_remainder(newstring_as_dict):
#obj, end = decoder.raw_decode(newstring_as_dict)
#remaining = input_data[end:]
#print (obj, end, remaining)

#actually the problem seems to be missing values
#try to use pandas to convert to df & fill NAs

read_as_dict = pandas.read_json(j)

print read_as_dict.head()

print read_as_dict.values



#read_as_series = pandas.Series(j)
#df = pandas.DataFrame(read_as_series)
#print read_as_series
#print df





