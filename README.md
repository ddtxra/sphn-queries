# Test for catalogue of queries

```
from sphn import SPHNRepository


sparql_endpoint = "http://vmld-01239:7200/repositories/"
repository = "hospfair"
catalog_uri = "https://raw.githubusercontent.com/ddtxra/sphn-queries/main/"

prefixes = {
    "sphn": "https://biomedit.ch/rdf/sphn-ontology/sphn#",
    "resource": "https://biomedit.ch/rdf/sphn-resource/"
}

repo = SPHNRepository(sparql_endpoint, repository, prefixes, catalog_uri)

```

```
df = repo.execute_query("core/2022/administrative_case", 10)```