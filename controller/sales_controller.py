from model.sales import sales
from view import terminal as view

HEADERS = sales.HEADERS

def list_transactions():
    view.print_table(sales.list_transactions_sales(), HEADERS)


def add_transaction():
    new_transaction = view.get_inputs(HEADERS[1:])
    sales.add_transaction_sales(new_transaction)


def get_unique_id():
    id_transaction_input = view.get_input(HEADERS[0])
    return id_transaction_input


def update_transaction():
    id_transaction = get_unique_id()
    if not sales.is_transaction_existing_sales(id_transaction):
        view.print_error_message("ID not found")
        return
    update_transaction_info = view.get_inputs(HEADERS[1:])

    sales.update_transaction_sales(id_transaction, update_transaction_info)


def delete_transaction():
    id_transaction = get_unique_id()
    if not sales.is_transaction_existing_sales(id_transaction):
        view.print_error_message("ID not found")
        return
    sales.delete_transaction_sales(id_transaction)
    view.print_message(f"Transaction {id_transaction} has been removed.")


def get_biggest_revenue_transaction():
    highest_revenue = sales.get_biggest_revenue_in_sales()
    view.print_general_results(highest_revenue, "Transaction with highest revenue")


def get_biggest_revenue_product():
    biggest_product_revenue = sales.biggest_revenue_in_product_sales()
    view.print_general_results(biggest_product_revenue, "Product with biggest revenue")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


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
