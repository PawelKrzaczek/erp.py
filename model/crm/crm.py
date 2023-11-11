""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
LIST = data_manager.read_table_from_file(DATAFILE)


def save_to_file():
    data_manager.write_table_to_file(DATAFILE, LIST)


def add_customer(customer):
    global LIST
    customer.insert(0, util.generate_id())
    LIST.append(customer)


def include(id):
    for i, row in enumerate(LIST):
        if id in row:
            return i
    return -1


def update_customer(customer, line):
    global LIST
    LIST[line][1], LIST[line][2], LIST[line][3] = customer[0], customer[1], customer[2]


def delete_customer(line):
    global LIST
    LIST.pop(line)


def emails():
    email = []
    for row in LIST:
        if '1' in row:
            email.append(row[2])
    return email
