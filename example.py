import dataConverter as dTj


URL = 'https://www.w3schools.com/python/module_requests.asp'
tableClass = 'w3-table-all notranslate'

#print(dTj.convertTableToJsonByClass(URL, tableClass, 'records'))
#print(dTj.convertTableToJsonByIndex(URL, 0, 'records'))

print(dTj.convertTableToCsvByIndex(URL, 0, 'records.csv'))
