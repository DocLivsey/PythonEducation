import sqlite3 as sql

connection = sql.connect('insurance_company.db')
clients = [(0, 'vova', 'chernov', '0123456789'), (1, 'daniil', 'lemeshko', '1234567890'),
           (2, 'nikita', 'pershin', '2345678901'), (3, 'oleg', 'gayvoronskiy', '3456789012'),
           (4, 'igor', 'gayvoronskiy', '4567890123'), (5, 'stanislav', 'gayvoronskiy', '5678901234'),
           (6, 'daniil', 'koschavtcev', '6789012345')]
contracts = [(74393471801, 0, 3, '2013-01-01', 102030.0), (120393471801, 2, 1, '2001-12-01', 234901.011),
             (24923803483, 0, 2, '2020-07-22', 1047394.23), (1203984310483, 5, 0, '2020-10-28', 75934.9),
             (3478384034, 6, 4, '2024-04-05', 1200.0)]
insurance_objects = [(0, 'hospital', ''), (1, 'bmw', ''), (2, 'mercedes', ''), (3, 'chicago', ''), (4, 'guitar', '')]
payments = [(0, '2013-01-01', 74393471801), (1, '2020-10-28', 1203984310483), (2, '2020-07-22', 24923803483),
            (3, '2001-12-01', 120393471801), (4, '2024-04-05', 3478384034)]

connection.cursor().executemany(
    'insert into Clients(id, first_name, last_name, passport) values (?,?,?,?)', clients)
connection.cursor().executemany(
    'insert into Contracts(contracts_№, client_id, object_id, contract_date, insurance_payment) '
    'values (?,?,?,?,?)', contracts)
connection.cursor().executemany(
    'insert into Insurance_Objects(id, object, description) values (?,?,?)', insurance_objects)
connection.cursor().executemany('insert into Insurance_Payments(id, date, contracts_№) values (?,?,?)', payments)
connection.commit()
connection.close()
