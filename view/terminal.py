def print_menu(title, list_options):

    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"{title}:")
    for i, elem in enumerate(list_options):
        print(f"({i}) {elem}")
    print()


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message, "\n")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    for row in range(len(label)):
        print(label[row], end=": ")
        print(result[row])
        print()


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    table.insert(0, headers)
    max_widths = [max(len(str(elem)) for elem in column) for column in zip(*table)]
    znak = "-"
    wynik = znak*sum(max_widths)+znak*(len(max_widths)*4)+znak*(len(max_widths)-1)
    print(f"/{wynik}\\")
    for row in table:
        print("|", end="")
        for elem, width in zip(row, max_widths):
            print(f"   {elem: <{width}} |", end="")
        print()
        print("|", end="")
        for elem, width in zip(row, max_widths):
            wynik = znak * width
            print(f"---{wynik}-|", end="")
        print()
    table.pop(0)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    inp = input(f"{label}: ")
    return inp


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    return [ input(f"{elem}: ") for elem in labels ]


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message, "\n")
