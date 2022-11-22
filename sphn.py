import requests
import pandas as pd
import urllib.parse

class SPHNRepository:

    def __init__(self, sparql_endpoint, repository, catalog_uri):
        self.sparql_endpoint = sparql_endpoint
        self.repository = repository
        self.catalog_uri = catalog_uri

    def replacePrefixes(self, s, prefixes):
        for k in prefixes.keys():
            s = s.replace(prefixes[k], k + ":")
        return s
    
    def execute_query(self, concept, limit, debug = False):
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
                   "Accept": "application/x-sparqlstar-results+json, application/sparql-results+json;"}

        url = self.sparql_endpoint + self.repository
        
        query = self.retrieve_query_from_catalog(concept)
        
        #TODO should be created automatically from parsing the PREFIX query lines
        prefixes = {
            "sphn": "https://biomedit.ch/rdf/sphn-ontology/sphn#",
            "resource": "https://biomedit.ch/rdf/sphn-resource/"
        }

        if(limit > 0):
            query = query + ("LIMIT " + str(limit))
        if(debug):
            print("querying...\n")
            print(query)
            print("\n")
            
        query_encoded = urllib.parse.quote(query)

        resp = requests.post(url=url, headers=headers, data="query=" + query_encoded)
        data = resp.json()
        
        if(debug):
            print("response:\n")
            print(data)
            
        column_headers =  data["head"]["vars"]
        lines = data["results"]["bindings"]
        
        lines_formatted = []
        for l in lines:
            o = {}
            for k in l.keys():
                if(l[k]["type"] == "uri"):
                    o[k] = self.replacePrefixes(l[k]["value"], prefixes)
                elif("datatype" in l[k] and l[k]["datatype"] == "http://www.w3.org/2001/XMLSchema#dateTime"):
                    o[k] = pd.to_datetime(l[k]["value"])
                else:
                    o[k] = str(l[k]["value"])
            lines_formatted.append(o)

            
        df = pd.DataFrame(lines_formatted, columns=column_headers)
        return df
    
    def retrieve_query_from_catalog(self, concept):
        uri = self.catalog_uri + concept + ".rq"
        res = requests.get(uri)
        return res.text