from bs4 import BeautifulSoup
import urllib2
import pandas

def read_page():
    """ url -> page source -> list of urls, titles (names, description, #rows)

    """

    pagename = "http://hub.healthdata.gov/dataset/hospital-compare-api"

    response = urllib2.urlopen(pagename)
    j = response.read()

    soup = BeautifulSoup(j)
    taglist = []
    titles = []

    for tag in soup.findAll('a', href=True):
        taglist.append(tag['href'])

    for tag in soup.findAll('a', title=True):
        titles.append(tag['title'])

    return taglist, titles


def filter_short_hits(taglist):
    """ choose urls that have resource IDs in them
    
    start with logic that resource ids are ~28 chars long
    """

    for tag in taglist[:]:
        if len(tag) < 28:
            taglist.remove(tag)

    return taglist

    
def string_has_num(word):
    """helper function to check whether string contains any numbers. returns true if numbers are present,
     false otherwise.

     #may be faster to replace this with a regex later?

    string --> bool

    >>> string_has_num("abcdef")
    False
    >>> string_has_num("12345")
    True
    >>> string_has_num("abc/1234")
    True

    """
    flag = False

    for char in word:
        if char.isdigit():
            flag = True
            break
    return flag


def return_datasets(taglist):
    """ identify strings that are links to datasets

    assumptions: if there are no numbers in the string and the word "resource" is absent, it's not a dataset

    """

    idlist = []

    # for tag in taglist[:]:
    #     if string_has_num(tag) == True: #if there is a number, assume it's a dataset, keep it
    #         continue                #do the next item in the for loop
    #     else:
    #         taglist.remove(tag)

    for tag in taglist:
        if "resource" in tag:
            idlist.append(tag)

    return idlist


def get_resourceid(idlist):
    """
     list of urls -> list of resource ids

     >>>get_resourceid("/dataset/hospital-compare-api/resource/88cd5782-a990-4668-8791-24b882cbfc52")
     88cd5782-a990-4668-8791-24b882cbfc52

    """
    residlist = []

    for url in idlist:
        resid = url.split('/')[-1]
        residlist.append(resid)

    return residlist


def remove_duplicates(residlist):
    """identify strings that appear more than once in the rawhitlist, and delete them.

    """
    unique_hits = []

    #would it be faster to convert to a dictionary?

    for item in residlist:
        #might be slow but try it this way first - just write out a new list
        if item not in unique_hits:
            unique_hits.append(item)

    return unique_hits


def write_df(titles, unique_hits):
    """ list of titles and resource ids -> return a df and write that to a csv file
    """

    df = pandas.DataFrame({'resource_id': unique_hits, 'description': titles}) #good to have to add column titles

    df.to_csv('dataset_identifiers.csv', sep= ";", index=False) #semicolons b/c there are commas in the titles

def scraped():
    taglist, titles = read_page()
    taglist = filter_short_hits(taglist)
    idlist = return_datasets(taglist)
    residlist = get_resourceid(idlist)
    unique_hits = remove_duplicates(residlist)
    write_df(titles, unique_hits)

scraped()