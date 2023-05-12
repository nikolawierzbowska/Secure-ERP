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
    print(title.upper())
    for index, option in enumerate(list_options[1:]):
        print(f"[{index + 1}]  {option}")
    print(f"[0]  {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print(label)
    print(result)


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/

def print_table(table,headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """

    column_widths = []
    for col in range(len(headers)):
        record_widths = []
        for row in range(len(table)):
            record_widths.append(len(table[row][col]))
        column_widths.append(max(record_widths) +2 )

    for row in range(len(table)):
        full_row = ''
        for col in range(len(headers)):
            full_row += table[row][col].center(column_widths[col]) + '|'
        print(full_row)
        if row == 0:
            print("-" * (sum(column_widths) + len(column_widths)))
    print("")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"{label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    print("Please provide data: ")
    list_of_labels = []
    for label in labels:
        get_user_input = input(f"{label}: ")
        list_of_labels.append(get_user_input)
    return list_of_labels


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("Error: ", message)
