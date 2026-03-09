import json
import openpyxl
import time
with open("test_data.json", "r") as file:
    chemistry_data = json.load(file)
workbook = openpyxl.load_workbook("heatlog_test.xlsx")
sheet = workbook.active
column_map = {
                      "C": "B",
                      "Mn": "C",
                      "P": "D",
                      "S": "E",
                      "Si": "F",
                      "Ni": "G",
                      "Cr": "H",
                      "Mo": "I",
                      "Cu": "J"
                 } 
row_map = {
                      "P1": 2,
                      "P2": 3,
                      "P3": 4,
                      "P4": 5,
                      "P5": 6
                 }
heat = input("Enter heat number")
while heat not in chemistry_data:
    with open("test_data.json", "r") as file:
        chemistry_data = json.load(file)
    print('Waiting for heat data')
    time.sleep(10)
while "P1" not in chemistry_data[heat] or "P2" not in chemistry_data[heat] or "P3" not in chemistry_data[heat]:
    with open("test_data.json", "r") as file:
        chemistry_data = json.load(file)
    if "P1"  not in chemistry_data[heat]:
        print("Waiting on P1")
        time.sleep(10)
    elif "P2" not in chemistry_data[heat]:
        print("Waiting on P2")
        time.sleep(5)
    elif "P3" not in chemistry_data[heat]:
        print("Waiting on P3")
        time.sleep(5)
for sample in chemistry_data[heat]:
    for element in chemistry_data[heat][sample]:
        column = column_map[element]
        row = row_map[sample]
        cell = column + str(row)
        value = chemistry_data[heat][sample][element]
        sheet[cell] = value
workbook.save("heatlog_test.xlsx")
print("Heatlog Complete")
# Mapping - Element = columns samples = rows
#main quest get test_data into the actual heatlog excel and change mapping according to new sheet 
#side quest - add time variations to continually check for samples until we reach our desired 3 sample minumum
#ex 10 minute retrys before "P1" and 5 minute checks after "P2"