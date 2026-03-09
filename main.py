import json
import openpyxl
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
if heat not in chemistry_data:
    print('Heat not found')
elif "P1" not in chemistry_data[heat] or "P2" not in chemistry_data[heat] or "P3" not in chemistry_data[heat]:
    print("Waiting on samples")

else:
    for sample in chemistry_data[heat]:
        for element in chemistry_data[heat][sample]:
            column = column_map[element]
            row = row_map[sample]
            cell = column + str(row)
            value = chemistry_data[heat][sample][element]
            sheet[cell] = value
    workbook.save("heatlog_test.xlsx")
# Mapping - Element = columns samples = rows
#main quest get test_data into an excel spreadsheet 
#side quest - use nested dictionaries to find the value of each samples chemistry