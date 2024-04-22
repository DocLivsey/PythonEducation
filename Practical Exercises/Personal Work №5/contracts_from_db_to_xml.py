import sqlite3 as sql
import xml.dom.minidom

connection = sql.connect("insurance_company.db")
doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

contracts_table_fields = ['contract_number', 'client_id', 'object_id', 'contract_date', 'insurance_payment']

all_contracts = connection.cursor().execute('SELECT * FROM contracts').fetchall()
for row in all_contracts:
    record = doc.createElement('record')
    root.appendChild(record)
    for _i in range(len(contracts_table_fields)):
        element = doc.createElement(contracts_table_fields[_i])
        element.appendChild(doc.createTextNode(str(row[_i])))
        record.appendChild(element)

with open('contracts_table_from_db.xml', 'w') as f:
    f.write(doc.toprettyxml())
