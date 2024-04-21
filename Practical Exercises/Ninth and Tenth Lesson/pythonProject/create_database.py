# − создать БД в соответствии с предметной областью «Туризм»,
# − БД должна содержать не менее двух связанных таблиц,
# − заполнить таблицы БД информацией с помощью SQL-запросов,
# − создать CGI-сервер
# − создать форму(формы) для заполнения полей таблиц

# − создать БД в соответствии с предметной областью «Туризм»,
# − БД должна содержать не менее двух связанных таблиц,
# − заполнить таблицы БД информацией с помощью SQL-запросов,
# − создать CGI-сервер
# − создать форму(формы) для заполнения полей таблиц,
# − осуществить вывод содержимого таблиц
# − экспорт/импорт таблицы в xml, используя заданную библиотеку

import sqlite3 as sql

connection = sql.connect('test.db')
cursor = connection.cursor()
cursor.execute(
    """create table if not exists Tourists (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) not null,
        last_name VARCHAR(30) not null);""")

cursor.execute(
    """create table if not exists Trips (
        id INTEGER PRIMARY KEY,
        city VARCHAR(30) not null,
        country VARCHAR(30) not null,
        description VARCHAR(300) not null);""")

cursor.execute(
    """create table if not exists Tourists_trips (
        tourist_id INTEGER not null,
        trip_id INTEGER not null,
        trip_date DATETIME not null,
        foreign key (tourist_id) references Tourists (id),
        foreign key (trip_id) references Trips (id));""")

connection.commit()
cursor.close()
connection.close()
