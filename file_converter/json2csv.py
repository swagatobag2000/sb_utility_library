import os
import json

def json2csv(jsonPath, fileName = None):
    try:
        filePath = ""
        filePath = os.path.dirname(jsonPath)+"\\output.csv" if fileName == None else os.path.dirname(jsonPath)+ "\\" + fileName + ".csv"

        with open(jsonPath, 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        keys = output.split(",")

        for obj in data:
            if list(obj.keys()) != keys:
                raise ValueError("JSON does not contain same set of keys. Cannot convert to CSV")

        for obj in data:
            output += f'\n'
            for key in keys:
                output += f'{obj[key]},'
            output = output[:-1]

        with open(filePath, 'w') as f:
            f.write(output)

    except ValueError as v:
        print("Exception: " + str(type(v)) +" "+ str(v))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")
    except Exception as e:
        print("Exception: " + str(type(e)) +" "+ str(e))
        print("1. Check the File Extension.")
        print("2. Check the Directory you entered.")

json2csv(r"C:\Users\Swagato\Downloads\input.json", "op")