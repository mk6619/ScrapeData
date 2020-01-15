import utils

#single function to do all work using tag class
def convertTableToJsonByClass(URL, tableClass, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tableClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

#single function to do all work using tag occurance index
def convertTableToJsonByIndex(URL, tagIndex, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

def convertTableToCsvByClass(URL, tableClass, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tableClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData

def convertTableToCsvByIndex(URL, tagIndex, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData
