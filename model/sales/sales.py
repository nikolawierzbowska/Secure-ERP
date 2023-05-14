""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def list_transactions_sales():
    transactions_base = data_manager.read_table_from_file(DATAFILE)
    transactions_base.insert(0, HEADERS)
    return transactions_base

def add_transaction_sales(record):
    transaction_base = data_manager.read_table_from_file(DATAFILE)
    record.insert(0, util.generate_id(transaction_base))
    update_list_of_transactions = data_manager.read_table_from_file(DATAFILE)
    update_list_of_transactions.append(record)
    data_manager.write_table_to_file(DATAFILE, update_list_of_transactions)

def is_transaction_existing_sales(id_sales):
    transactions = data_manager.read_table_from_file(DATAFILE)
    for transaction in transactions:
        if id_sales == transaction[0]:
            return True
    return False

def update_transaction_sales(id_sales, transaction_data):
    transactions = data_manager.read_table_from_file(DATAFILE)
    for index, transaction in enumerate(transactions):
        if id_sales == transaction[0]:
            del transactions[index]
            transactions.insert(index, [id_sales, *transaction_data])
    data_manager.write_table_to_file(DATAFILE, transactions)

def delete_transaction_sales(id_sales):
    transactions = data_manager.read_table_from_file(DATAFILE)
    for index, transaction in enumerate(transactions):
        if id_sales == transaction[0]:
            del transactions[index]
    data_manager.write_table_to_file(DATAFILE, transactions)

def get_biggest_revenue_in_sales():
    transactions = data_manager.read_table_from_file(DATAFILE)
    transactions_in_revenue_list = []
    for transaction in transactions:
        transactions_in_revenue_list.append(float(transaction[3]))
    biggest_revenue = max(transactions_in_revenue_list)
    for transaction in transactions:
        if float(transaction[3]) == biggest_revenue:
            return transaction

def biggest_revenue_in_product_sales():
    # transactions = data_manager.read_table_from_file(DATAFILE)
    # transactions_in_product_revenue = []
    # for transaction in transactions:
    #     transactions_in_product_revenue.append(f"{transaction[2]}, {transaction[3]}")
    # for products in set(transactions_in_product_revenue):
    #     number_of_products = transactions_in_product_revenue.count(products)
    # print(transactions_in_product_revenue)
    pass
