#encoding: UTF-8
import terminaltables
import frecuencias
import jiCuadrada


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

def createCustomTable(text):
    dictTable = frecuencias.frecuenciaLetras(text)
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(['Processed Char', 'Average count'])
    for n in range(len(dictTable)):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.AsciiTable(data)
    table.title = "Tabla de Frecuenia"
    return table.table

def createJiTable(dictionary):
    dictTable = dictionary
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(["Swap index", "JI"])
    for n in range(len(dictTable)):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.AsciiTable(data)
    table.title = "JI Cuadrada"
    return table.table


