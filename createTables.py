#encoding: UTF-8
import terminaltables
import frecuencias


def createSampleTable():
    dictTable = frecuencias.frecuencias()
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(['Processed Char', 'Average count'])
    for n in range(26):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.AsciiTable(data)
    table.title = "Tabla de Frecuencias"
    return table.table

def createCustomTable(text):
    dictTable = frecuencias.frecuenciaLetras(text)
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(['Processed Char', 'Average count'])
    for n in range(len(dictTable)):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.AsciiTable(data)
    table.title = "Tabla de frecuencias"
    return table.table