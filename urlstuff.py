import urllib2
import urllib
import json

def dataget():
    url= "http://api.thriftdb.com/api.hnsearch.com/items/_search?"
    reqdata = {"q": "pg","weights[title]":0.1,"weights[username]":100}
    reqstring= urllib.urlencode(reqdata)
    response =  urllib2.urlopen(url+reqstring)
    data = json.loads(response.read())
    return data 

results = dataget()["results"]
for item in results:
    print item["item"]
