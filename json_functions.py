import csv
import json

dct = {}

def csv_to_json():
    with open("all_final.csv", 'r', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        for index, row in enumerate(csv_data, start=0):
            dct[index] = row[0]

    with open("facts.json", 'w') as json_file:
        json.dump(dct, json_file, indent=4)

def load_json():
    with open('facts.json', 'r') as j:
        return json.load(j)


