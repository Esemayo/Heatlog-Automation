import json
with open("test_data.json", "r") as file:
    chemistry_data = json.load(file)
for heat in chemistry_data:
        print([heat])
        for sample in chemistry_data[heat]:
            print([sample])
            for element in chemistry_data[heat][sample]:
                 print(chemistry_data[heat][sample][element])
#main quest get test_data into an excel spreadsheet 
#side quest - use nested dictionaries to find the value of each samples chemistry