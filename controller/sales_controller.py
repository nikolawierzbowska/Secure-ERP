from model.sales import sales
from view import terminal as view
import datetime

HEADERS = sales.HEADERS


def list_transactions():
    view.print_table(sales.list_transactions_sales(), HEADERS)


def get_customer_id():
    id_customer_input = view.get_input(HEADERS[1])
    return id_customer_input


def validate_customer_id():
    while True:
        id_customer = get_customer_id()
        if not sales.is_customer_id_existing_sales(id_customer):
            view.print_error_message("ID not found")
            continue
        return id_customer


def validate_price():
    while True:
        try:
            price = view.get_input(HEADERS[3])
            price = float(price)
            return str(price)
        except ValueError:
            view.print_message("Invalid price ")


def validate_dates():
    view.print_message("Enter the dates in YYYY-MM-DD format: ")
    while True:
        try:
            date = view.get_input(HEADERS[4])
            if datetime.datetime.strptime(date, '%Y-%m-%d') and datetime.datetime.strptime(date,
                                                                                           '%Y-%m-%d').date() <= datetime.datetime.now().date():
                return date
            else:
                view.print_message("Enter the dates in YYYY-MM-DD format: ")
                continue
        except ValueError:
            view.print_message("Invalid date format. Please use YYYY-MM-DD format")


def get_information_about_transaction():
    new_transaction = [validate_customer_id(), view.get_input(HEADERS[2]), validate_price(), validate_dates()]
    return new_transaction


def add_transaction():
    view.print_table(sales.list_transactions_sales(), HEADERS)
    new_transaction = get_information_about_transaction()
    sales.add_transaction_sales(new_transaction)
    view.print_message(f"Transaction {new_transaction} has been added.")


def get_unique_id():
    id_transaction_input = view.get_input(HEADERS[0])
    return id_transaction_input


def update_transaction():
    view.print_table(sales.list_transactions_sales(), HEADERS)
    id_transaction = get_unique_id()
    if not sales.is_transaction_existing_sales(id_transaction):
        view.print_error_message("ID not found")
        return
    update_transaction_info = get_information_about_transaction()
    sales.update_transaction_sales(id_transaction, update_transaction_info)
    view.print_message(f"Transaction {id_transaction} has been updated.")


def delete_transaction():
    view.print_table(sales.list_transactions_sales(), HEADERS)
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
    date_1 = validate_dates()
    date_2 = validate_dates()
    number_of_transactions = sales.count_transactions_between_sales(date_1, date_2)
    view.print_general_results(number_of_transactions, "The number of transactions between two dates")


def sum_transactions_between():
    date_1 = validate_dates()
    date_2 = validate_dates()
    sum_the_price_of_transactions = sales.sum_transactions_between_sales(date_1, date_2)
    view.print_general_results(sum_the_price_of_transactions, "Sum the price of transactions between two dates")


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
