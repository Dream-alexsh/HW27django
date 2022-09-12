# import csv
# import json
#
#
# def csv_to_json(csvFilePath, model_name, jsonFilePath):
#     jsonArray = []
#
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)
#
#         for row in csvReader:
#             to_add = {'model': model_name, 'pk': int(row['Id'])}
#             del row['Id']
#             if row['is_published'] == 'TRUE':
#                 row['is_published'] = True
#             else:
#                 row['is_published'] = False
#             if 'price' in row:
#                 row['price'] = int(row['price'])
#             if 'author_id' in row:
#                 row['author_id'] = int(row['author_id'])
#             if 'category_id' in row:
#                 row['category_id'] = int(row['category_id'])
#             to_add['fields'] = row
#             jsonArray.append(to_add)
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonfile:
#         jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
#         jsonfile.write(jsonString)
#
#
# def csv_to_json_2(csvFilePath, model_name, jsonFilePath):
#     jsonArray = []
#
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)
#
#         for row in csvReader:
#             to_add = {'model': model_name, 'pk': int(row['id']), 'fields': row}
#             if 'lat' in row:
#                 row['lat'] = float(row['lat'])
#             if 'lng' in row:
#                 row['lng'] = float(row['lng'])
#             if 'age' in row:
#                 row['age'] = int(row['age'])
#             if 'location_id' in row:
#                 row['location_id'] = int(row['location_id'])
#             del row['id']
#             jsonArray.append(to_add)
#
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonfile:
#         jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
#         jsonfile.write(jsonString)
#
#
# csvFilePath = r'datasets/ad.csv'
# jsonFilePath = r'fixtures/ad.json'
# csvFilePath_1 = r'datasets/category.csv'
# jsonFilePath_1 = r'fixtures/category.json'
# csvFilePath_2 = r'datasets/location.csv'
# jsonFilePath_2 = r'fixtures/location.json'
# csvFilePath_3 = r'datasets/user.csv'
# jsonFilePath_3 = r'fixtures/user.json'
#
#
# csv_to_json(csvFilePath, 'ads.ad', jsonFilePath)
# csv_to_json_2(csvFilePath_1, 'ads.category', jsonFilePath_1)
# csv_to_json_2(csvFilePath_2, 'ads.location', jsonFilePath_2)
# csv_to_json_2(csvFilePath_3, 'ads.user', jsonFilePath_3)
import datetime


y = datetime.date.today()-datetime.date(2001, 0o1, 0o1)
print(int(y.total_seconds() / (3600*24*365)))


day = str(datetime.date.today()).split('-')
day = int(day[0])
print(day)
# print(datetime(year=2022, month=5, day=10))

