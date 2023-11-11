""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from datetime import datetime

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
LIST = data_manager.read_table_from_file(DATAFILE)


def save_to_file():
    data_manager.read_table_from_file(DATAFILE, LIST)


def add_employee(employee):
    global LIST
    employee.insert(0, util.generate_id())
    LIST.append(employee)


def include(id_):
    for i, row in enumerate(LIST):
        if id_ in row:
            return i
    return -1


def update_employee(employee, line):
    global LIST
    LIST[line][1], LIST[line][2], LIST[line][3], LIST[line][4] = employee[0], employee[1], employee[2], employee[3]


def delete_employee(line):
    global LIST
    LIST.pop(line)


def get_oldest_and_youngest():
    date_format = '%Y-%m-%d'

    max_, min_ = LIST[0], LIST[0]
    for row in LIST:
        date1 = datetime.strptime(max_[2], date_format)
        date2 = datetime.strptime(min_[2], date_format)
        date3 = datetime.strptime(row[2], date_format)
        if date1 < date3:
            max_ = row
        elif date2 > date3:
            min_ = row
    print("OLDEST", max_)
    print("YOUNGEST", min_)


def get_average_age():
    print("Average:", sum(int(row[2]) for row in LIST) / len(LIST))


def next_birthdays(data):
    BIRTHDAY = []
    date_format = '%Y-%m-%d'
    for row in LIST:
        date1 = datetime.strptime(row[2], date_format)
        date2 = datetime.strptime(data, date_format)
        if (date1 - date2).days <= 14:
            BIRTHDAY.append(row[1])
    print(BIRTHDAY)


def count_employees_with_clearance(level):
    greater_tha_level = 0
    for elem in LIST:
        if int(elem[4]) >= level:
            greater_tha_level += 1
    print(greater_tha_level)


def count_employees_per_department():
    company = {}
    for row in LIST:
        if row[3] not in company:
            company[row[3]] = 1
        else:
            company[row[3]] += 1
    print(company)
