import pandas
import requests
from bs4 import BeautifulSoup

def getDataFromUrl(url):
    return requests.get(url)

def parseDataUsingHtmlParser(page):
    return BeautifulSoup(page.content, 'html.parser')

def findTableByClass(soup, tagId, tableClass):
    return soup.find(tagId, { "class" : tableClass })

def findTableByIndex(soup, tagId, tagIndex):
    return soup.findAll(tagId)[tagIndex]

def convertTableToList(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

def convertListToJson(dataList, orientation):
    df = pandas.DataFrame(dataList)
    if orientation == 'none':
        return df.to_json()
    else:
        return df.to_json(orient='records')

def convertTableToJsonByClass(URL, tableClass, orientation, tagId = "table"):
    return convertListToJson(convertTableToList(findTableByClass(parseDataUsingHtmlParser(getDataFromUrl(URL)),tagId, tableClass)), orientation)

def convertTableToJsonByIndex(URL, tagIndex, orientation, tagId = "table"):
    return convertListToJson(convertTableToList(findTableByIndex(parseDataUsingHtmlParser(getDataFromUrl(URL)),tagId, tagIndex)), orientation)
