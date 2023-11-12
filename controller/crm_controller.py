from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_table(crm.LIST, crm.HEADERS)
    # view.print_general_results(crm.LIST, crm.HEADERS)


def add_customer():
    crm.add_customer(view.get_inputs(crm.HEADERS[1:]))


def update_customer():
    id_ = view.get_input("Select an id of customer")
    line = crm.include(id_)
    if line >= 0:
        crm.update_customer(view.get_inputs(crm.HEADERS[1:]), line)


def delete_customer():
    id_ = view.get_input("Select an id of customer")
    line = crm.include(id_)
    if line >= 0:
        crm.delete_customer(line)


def get_subscribed_emails():
    view.print_general_results(crm.emails()[0], crm.emails()[1])


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        crm.save_to_file()
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
