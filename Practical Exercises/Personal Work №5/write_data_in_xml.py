import xml.dom.minidom

doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

data = [
    {"id": "524952582", "first_name": "fsfwfwfr", "last_name": "Black", "passport": "12523556"},
    {"id": "4262623573592", "first_name": "Jane", "last_name": "White", "passport": "75215293"},
    {"id": "34223463464234", "first_name": "Donald", "last_name": "Duck", "passport": "828252516"}
]
for row in data:
    record = doc.createElement('record')
    root.appendChild(record)
    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(value))
        record.appendChild(element)

with open('table.xml', 'w') as f:
    f.write(doc.toprettyxml())
