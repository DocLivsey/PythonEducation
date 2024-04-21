import sqlite3 as sql

connection = sql.connect('test.db')
cursor = connection.cursor()
people = [("lemeshko", "daniil"), ("nolan", "christopher"), ("chernov", "vova"), ("pershin", "nikita")]
locations = {"russia": ["moscow", "sochi"], "japan": ["tokio", "kyoto"], "germany": ["berlin", "hamburg"]}

i = 0
for human in people:
    i += 1
    human_tuple = (i, human[0], human[1])
    cursor.execute('insert into Tourists(id, first_name, last_name) values (?, ?, ?)', human_tuple)

i = 0
for location in locations.items():
    for city in locations[location[0]]:
        i += 1
        location_tuple = (i, city, location[0], "")
        cursor.execute(
            'insert into Trips (id, city, country, description) values (?, ?, ?, ?)', location_tuple)

trips = [(1, 1, "2003-11-12"), (2, 2, "2013-09-22"), (3, 1, "2019-03-28"), (4, 2, "2021-07-03")]
cursor.executemany('insert into Tourists_trips(tourist_id, trip_id, trip_date) values (?, ?, ?)', trips)

connection.commit()
cursor.close()
connection.close()
