import csv


def importFile(fileName, fileType):
    dataList = []
    if fileType == "CSV":
        with open(fileName, newline="") as csv_file:
            reader = csv.reader(csv_file)
            dataList = list(reader)
    elif fileType == "TSV":
        with open(fileName, newline="") as csv_file:
            reader = csv.reader(csv_file, delimiter="\t")
            dataList = list(reader)
    elif fileType == "XLSX":
        import xlrd

        workbook = xlrd.open_workbook(fileName)
        worksheet = workbook.sheet_by_index(0)
        dataList = []
    elif fileType == "XLS":
        import xlrd

        workbook = xlrd.open_workbook(fileName)
        worksheet = workbook.sheet_by_index(0)
        dataList = []
        for row in range(worksheet.nrows):
            dataList.append(worksheet.row_values(row))
    return dataList


def importDirectory(directory):
    import os

    datalist = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            datalist.append(importFile(directory + "/" + file, "CSV"))
        elif file.endswith(".tsv"):
            datalist.append(importFile(directory + "/" + file, "TSV"))
        elif file.endswith(".xlsx"):
            datalist.append(importFile(directory + "/" + file, "XLSX"))
        elif file.endswith(".xls"):
            datalist.append(importFile(directory + "/" + file, "XLS"))
    return datalist
