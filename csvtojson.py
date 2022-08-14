import csv
import json


def csv_to_json(csvFilePath, model_name, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            to_add = {'model': model_name, 'pk': int(row['Id'])}
            del row['Id']
            if row['is_published'] == 'TRUE':
                row['is_published'] = True
            else:
                row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            to_add['fields'] = row
            jsonArray.append(to_add)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonfile:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonfile.write(jsonString)


def csv_to_json_2(csvFilePath, model_name, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            to_add = {'model': model_name, 'pk': int(row['id']), 'fields': row}
            del row['id']
            jsonArray.append(to_add)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonfile:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonfile.write(jsonString)


csvFilePath = r'datasets/ads.csv'
jsonFilePath = r'fixtures/ads.json'
csvFilePath1 = r'datasets/categories.csv'
jsonFilePath1 = r'fixtures/categories.json'

csv_to_json(csvFilePath, 'ads.ad', jsonFilePath)
csv_to_json_2(csvFilePath1, 'ads.category', jsonFilePath1)