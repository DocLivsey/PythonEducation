import sqlite3 as sql
import xml.dom.minidom

connection = sql.connect("insurance_company.db")
doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

clients_table_fields = ['id', 'first_name', 'last_name', 'passport']

all_clients = connection.cursor().execute('SELECT * FROM clients').fetchall()
for row in all_clients:
    record = doc.createElement('record')
    root.appendChild(record)
    for _i in range(len(clients_table_fields)):
        element = doc.createElement(clients_table_fields[_i])
        element.appendChild(doc.createTextNode(str(row[_i])))
        record.appendChild(element)

with open('clients_table_from_db.xml', 'w') as f:
    f.write(doc.toprettyxml())
