import pandas
import requests
from bs4 import BeautifulSoup

#sends HTTP request to a url
def getDataFromUrl(url):
    return requests.get(url)

#Parse HTML data using beautiful soup library
def parseDataUsingHtmlParser(page):
    return BeautifulSoup(page.content, 'html.parser')

#find tag by its class
def findTableByClass(soup, tagId, tableClass):
    return soup.find(tagId, { "class" : tableClass })

#find tag by its index
def findTableByIndex(soup, tagId, tagIndex):
    return soup.findAll(tagId)[tagIndex]

#convert table data to list
def convertTableToList(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

#convert list to json
#using orientation we can convert list to json row wise or column wise
#options available are as follows:-

"""
‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}

‘records’ : list like [{column -> value}, … , {column -> value}]

‘index’ : dict like {index -> {column -> value}}

‘columns’ : dict like {column -> {index -> value}}

‘values’ : just the values array

‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data, and the data component is like orient='records'.
"""

def convertListToJson(dataList, orientation):
    df = pandas.DataFrame(dataList)
    if orientation == 'none':
        return df.to_json()
    else:
        return df.to_json(orient='records')

#a single function to do all work by taking tag class as input
def convertTableToJsonByClass(URL, tableClass, orientation, tagId = "table"):
    return convertListToJson(convertTableToList(findTableByClass(parseDataUsingHtmlParser(getDataFromUrl(URL)),tagId, tableClass)), orientation)

#a single function to do all work by taking tag index as input
def convertTableToJsonByIndex(URL, tagIndex, orientation, tagId = "table"):
    return convertListToJson(convertTableToList(findTableByIndex(parseDataUsingHtmlParser(getDataFromUrl(URL)),tagId, tagIndex)), orientation)
