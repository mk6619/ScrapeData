import pandas
import requests
from bs4 import BeautifulSoup

#sends HTTP request to a url
def getDataFromUrl(url):
    return requests.get(url)

#parse HTML data using beautiful soup library
def parseDataUsingHtmlParser(page):
    return BeautifulSoup(page.content, 'html.parser')

#find tag by its class
def findTableByClass(soup, tagId, tagClass):
    return soup.find(tagId, { "class" : tagClass })

#find tag by its occurance index
def findTableByIndex(soup, tagId, tagIndex):
    return soup.findAll(tagId)[tagIndex]

#converts table data to list
def convertTableToList(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

#converts list to json
#options available for orientation
"""
‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
‘records’ : list like [{column -> value}, … , {column -> value}]
‘index’ : dict like {index -> {column -> value}}
‘columns’ : dict like {column -> {index -> value}}
‘values’ : just the values array
‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data, and the data component is like orient='records'.
"""
def convertListToJson(dataList, orientation = 'none'):
    df = pandas.DataFrame(dataList)
    if orientation == 'none':
        return df.to_json()
    else:
        return df.to_json(orient = orientation)

#converts list to csv
def convertListToCsv(dataList, fileName):
    df = pandas.DataFrame(dataList)
    return df.to_csv(fileName)
