import pandas
import requests
from bs4 import BeautifulSoup

def getDataFromUrl(url):
    return requests.get(url)

def parseDataUsingHtmlParser(page):
    return BeautifulSoup(page.content, 'html.parser')

def findTable(soup, tableId, tableClass):
    return soup.find(tableId, { "class" : tableClass })

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

def convertTableFromUrlToJson(URL, tableClass, orientation, tableId = "table"):
    return convertListToJson(convertTableToList(findTable(parseDataUsingHtmlParser(getDataFromUrl(URL)),tableId, tableClass)), orientation)

