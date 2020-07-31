from ScrapeData import utils

#single function to convert to json using tag class
def convertTableToJsonByClass(URL, tagClass, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tagClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

#single function to convert to json using tag occurance index
def convertTableToJsonByIndex(URL, tagIndex, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

#single function to convert to csv using tag class
def convertTableToCsvByClass(URL, tagClass, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tagClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData

#single function to convert to csv using tag occurance index
def convertTableToCsvByIndex(URL, tagIndex, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData
