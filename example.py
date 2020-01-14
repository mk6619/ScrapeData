import dataToJson as dTj


URL = input("Enter url: ")
tableClass = input("Enter tableID: ")

print(dTj.convertTableFromUrlToJson(URL, tableClass, 'records'))
