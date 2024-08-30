# Найти количество парковок каждого типа на заданном участке карты.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import xmltodict
import re


'''
left_down = tuple(map(lambda coordinate: float(coordinate),
                      input('enter separated by comma left down border of map - ').split(',')))
right_up = tuple(map(lambda coordinate: float(coordinate),
                     input('enter separated by comma right up border of map - ').split(',')))
lat_left = left_down[0]
lon_left = left_down[1]

lat_right = right_up[0]
lon_right = right_up[1]'''

lat_left = 68.6593442
lon_left = 33.1000237
lat_right = 69.9593442
lon_right = 35.1283237


def isInsideRectangle(lat, lon):
    return lat_left <= lat <= lat_right and lon_left <= lon <= lon_right


def findParking(xml_dict):
    _k = 0
    for node in dct['osm']['node']:
        _lat = float(node['@lat'])
        _lon = float(node['@lon'])
        if isInsideRectangle(_lat, _lon):
            if 'tag' in node and isinstance(node['tag'], list):
                for tag in node['tag']:
                    if tag['@k'] == 'amenity' and re.match(template, tag['@v']):
                        _k += 1
            elif 'tag' in node and isinstance(node['tag'], dict):
                if node['tag']['@k'] == 'amenity' and re.match(template, node['tag']['@v']):
                    _k += 1
    return _k


'''
    Находим просто количество парковок (по всей карте)
'''

template = r'.*parking.*'

fin = open('osm/12.osm', 'r', encoding='utf-8')
fin_2 = open('osm/12 -2.osm', 'r', encoding='utf-8')
dct = xmltodict.parse(fin.read())
dct_2 = xmltodict.parse(fin_2.read())
k = findParking(dct)
k += findParking(dct_2)
print(k)

fin.close()
fin_2.close()
