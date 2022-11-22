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
df = repo.execute_query("core/2022/administrative_case", 10)
```


with seaborn
```
import seaborn as sns
import pandas as pd
import numpy as np

keys = ['origin_location_class', 'origin_location']
fig, axs = plt.subplots(len(keys), figsize=(20, 10))
for i in range(len(keys)):
    df_counts = pd.DataFrame(df.value_counts(keys[i], dropna=False))
    df_counts = df_counts.reset_index().rename({0: 'count'}, axis=1)
    df_counts = df_counts.replace(np.nan, 'nan')
    sns.barplot(data=df_counts, x="count", y=keys[i], ax=axs[i])
```

with matplot lib
```
import matplotlib.pyplot as plt
keys = ['origin_location_class', 'origin_location']
fig, axs = plt.subplots(len(keys), figsize=(20, 10))
for i in range(len(keys)):
    df.value_counts(keys[i], dropna=False).plot(kind='barh', ax=axs[i], subplots=True)
    plt.title(keys[i])
    plt.tight_layout()
    
```


```
sns.histplot(df_plot['admission_date_time'], bins=50)
```

```
df_plot = df.replace(np.nan, 'nan')
keys = ['origin_location_class', 'origin_location']
fig, axs = plt.subplots(len(keys), figsize=(20, 10))
for i in range(len(keys)):
    sns.countplot(y=df_plot[keys[i]], ax=axs[i])
```

```
sns.histplot((df_plot['discharge_date_time'] - df_plot['admission_date_time']).dt.days)
plt.xlim([-20, 500])
```

