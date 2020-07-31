import Utils

#single function to convert to json using tag class
def toJsonByClass(URL, tagClass, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tagClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

#single function to convert to json using tag occurance index
def toJsonByIndex(URL, tagIndex, orientation, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToJson(listData, orientation)
    return jsonData

#single function to convert to csv using tag class
def toCsvByClass(URL, tagClass, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByClass(parsedData,tagId, tagClass)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData

#single function to convert to csv using tag occurance index
def toCsvByIndex(URL, tagIndex, fileName, tagId = "table"):
    responseData = utils.getDataFromUrl(URL)
    parsedData = utils.parseDataUsingHtmlParser(responseData)
    tableData = utils.findTableByIndex(parsedData,tagId, tagIndex)
    listData = utils.convertTableToList(tableData)
    jsonData = utils.convertListToCsv(listData, fileName)
    return jsonData
