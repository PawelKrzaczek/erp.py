from model.sales import sales
from view import terminal as view


def list_transactions():
    view.print_table(sales.LIST_SALES, sales.HEADERS)
    # view.print_general_results(sales.LIST_SALES, sales.HEADERS)


def add_transaction():
    sales.add_transaction(view.get_inputs(sales.HEADERS[1:]))


def update_transaction():
    id_ = view.get_input("Select an id of transaction")
    line = sales.include(id_)
    if line >= 0:
        sales.update_transaction(view.get_inputs(sales.HEADERS[1:]), line)


def delete_transaction():
    id_ = view.get_input("Select an id of transaction")
    line = sales.include(id_)
    if line >= 0:
        sales.delete_transaction(line)


def get_biggest_revenue_transaction():
    view.print_table(sales.biggest_transaction())


def get_biggest_revenue_product():
    sales.biggest_product()


def count_transactions_between():
    data_start = view.get_input("Start date: ")
    data_end = view.get_input("End date: ")
    sales.count_between(data_start, data_end)


def sum_transactions_between():
    data_start = view.get_input("Start date: ")
    data_end = view.get_input("End date: ")
    sales.sum_between(data_start, data_end)


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        sales.save_to_file()
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
