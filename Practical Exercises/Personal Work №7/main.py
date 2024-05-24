# Найти количество людей, выполнивших тест более чем за заданное время
# и набравших ровно 9 баллов. Вывести их список.

import csv
from datetime import datetime


def parseTime(str_time: str):
    split = str_time.split('.')
    time_dict = {}
    for time_unit in split:
        if len(time_unit) > 0:
            time_dict[time_unit.split()[1]] = time_unit.split()[0]
    hour = 0
    minutes = 0
    sec = 0
    if 'ч' in time_dict.keys():
        hour = time_dict['ч']
    if 'мин' in time_dict.keys():
        minutes = time_dict['мин']
    if 'сек' in time_dict.keys():
        sec = time_dict['сек']
    _time = f'{hour}:{minutes}:{sec}'
    return datetime.strptime(_time, template).time()


template = '%H:%M:%S'
time = input('input time in format - Hours:Minutes:Seconds - ')
#time = '0:10:0'
time = datetime.strptime(time, template).time()
print(time)

first_csv = open('csv/12 - 1.csv', encoding='utf-8')
second_csv = open('csv/12 - 2.csv', encoding='utf-8')

data_from_first_csv = csv.DictReader(first_csv, delimiter=',')
data_from_second_csv = csv.DictReader(second_csv, delimiter=',')

people = []
for row in data_from_first_csv:
    spent_time = parseTime(row['Затраченное время'])
    if spent_time > time:
        if row['Оценка/10,00'] == '9,00':
            people.append({'name': f'{row['Фамилия']} {row['Имя']}',
                           'mark': row['Оценка/10,00'],
                           'spent time': spent_time})

for row in data_from_second_csv:
    spent_time = parseTime(row['Затраченное время'])
    if spent_time > time:
        if row['Оценка/100,00'] == '90,00':
            people.append({'name': f'{row['Фамилия']} {row['Имя']}',
                           'mark': row['Оценка/100,00'],
                           'spent time': spent_time})

for men in people:
    print(men)
