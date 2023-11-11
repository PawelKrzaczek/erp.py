from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_general_results(hr.LIST, hr.HEADERS)


def add_employee():
    hr.add_employee(view.get_inputs(hr.HEADERS[1:]))


def update_employee():
    id_ = view.get_input("Select an id of transaction")
    line = hr.include(id_)
    if line >= 0:
        hr.update_employee(view.get_inputs(hr.HEADERS[1:]), line)


def delete_employee():
    id_ = view.get_input("Select an id of transaction")
    line = hr.include(id_)
    if line >= 0:
        hr.delete_employee(line)


def get_oldest_and_youngest():
    hr.get_oldest_and_youngest()


def get_average_age():
    hr.get_average_age()


def next_birthdays():
    data = view.get_input("Start date: ")
    hr.next_birthdays(data)


def count_employees_with_clearance():
    level = view.get_input("Get clearance lvl: ")
    hr.count_employees_with_clearance(level)


def count_employees_per_department():
    hr.count_employees_per_department()


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        hr.save_to_file()
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
