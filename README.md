# ScrapeData
Python module to get table data from any webpage and converts it into either Json or Csv

## Installation
Supported python version is 3.0+
```
pip3 install ScrapeData
```


## Usage
There are 4 functions exposed which will do all the work for you available in **dataConverter**
```
1. convertTableToJsonByClass(URL, tagClass, orientation, tagId = "table")
2. convertTableToJsonByIndex(URL, tagIndex, orientation, tagId = "table")
3. convertTableToCsvByClass(URL, tagClass, fileName, tagId = "table")
4. convertTableToCsvByIndex(URL, tagIndex, fileName, tagId = "table")
```

1. **URL** :- The url from where table needs to fetched
2. **tagClass** :- if there is any class associated with tag
3. **tagIndex** :- the occurance index of the table you want to fetch.
4. **tagId** :- the html tag which is by default table
5. **orientation** :- 
```
‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
‘records’ : list like [{column -> value}, … , {column -> value}]
‘index’ : dict like {index -> {column -> value}}
‘columns’ : dict like {column -> {index -> value}}
‘values’ : just the values array
‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data, and the data component is like orient='records'.
```
There are other functions available in **utils** if you want to customize the implementation.
```
1. getDataFromUrl(url)
2. parseDataUsingHtmlParser(page)
3. findTableByClass(soup, tagId, tagClass)
4. findTableByIndex(soup, tagId, tagIndex)
5. convertTableToList(table)
6. convertListToJson(dataList, orientation = 'none')
7. convertListToCsv(dataList, fileName)
```

## Example Code

```
from ScrapeData import dataConverter as dc
from ScrapeData import utils

URL = 'https://www.w3schools.com/python/module_requests.asp'
tableClass = 'w3-table-all notranslate'

print(dc.convertTableToJsonByClass(URL, tableClass, 'records'))
print(dc.convertTableToJsonByIndex(URL, 0, 'records'))
print(dc.convertTableToCsvByIndex(URL, 0, 'records.csv'))
```
