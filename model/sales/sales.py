""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
from datetime import datetime

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
LIST_SALES = data_manager.read_table_from_file(DATAFILE)


def save_to_file():
    data_manager.write_table_to_file(DATAFILE, LIST_SALES)


def add_transaction(transaction):
    global LIST_SALES
    transaction.insert(0, util.generate_id())
    LIST_SALES.append(transaction)


def include(id_):
    for i, row in enumerate(LIST_SALES):
        if id_ in row:
            return i
    return None


def update_transaction(transaction, line):
    global LIST_SALES
    LIST_SALES[line][1], LIST_SALES[line][2], LIST_SALES[line][3], LIST_SALES[line][4] = transaction[0], transaction[1], transaction[2], transaction[3]


def delete_transaction(line):
    global LIST_SALES
    LIST_SALES.pop(line)


def biggest_transaction():
    max_ = LIST_SALES[0]
    for row in LIST_SALES:
        if float(max_[3]) < float(row[3]):
            max_ = row
    return max_, HEADERS


def biggest_product():
    max_revenue = {}
    for row in LIST_SALES:
        if row[2] not in max_revenue:
            max_revenue[row[2]] = float(row[3])
        else:
            max_revenue[row[2]] += float(row[3])

    top_product = max(max_revenue, key=max_revenue.get)
    return [top_product, max_revenue[top_product]], [HEADERS[2], HEADERS[3]]


def date_between(data_start, data_end, data_middle):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(data_start, date_format)
    date2 = datetime.strptime(data_end, date_format)
    date3 = datetime.strptime(data_middle, date_format)
    if date1 <= date3 <= date2:
        return True
    return False


''' # Extract day, month, and year from date strings
        day1, month1, year1 = int(date_str1[:2]), int(date_str1[3:5]), int(date_str1[6:])
        day2, month2, year2 = int(date_str2[:2]), int(date_str2[3:5]), int(date_str2[6:])
        day3, month3, year3 = int(date_str3[:2]), int(date_str3[3:5]), int(date_str3[6:])

        if year1 == year2 == year3:
            if month1 == month2 == month3:
                if day1 <= day3 <= day2:
                    print("yes")
            elif month1 <= month3 <= month2:
                print("yes")
        elif year1 <= year2 <= year3:
            print("yes")

        if (year1 == year2 == year3) and (
                (month1 == month2 == month3 and day1 <= day3 <= day2) or (month1 <= month3 <= month2)) or (
                year1 <= year2 <= year3):
            print("yes")
'''


def count_between(data_start, data_end):
    count = 0

    for row in LIST_SALES:
        if date_between(data_start, data_end, row[4]):
            count += 1
    return [count], ["DAYS"]


def sum_between(data_start, data_end):
    sum_ = 0

    for row in LIST_SALES:
        if date_between(data_start, data_end, row[4]):
            sum_ += float(row[3])
    return [sum_], ["SUM"]
