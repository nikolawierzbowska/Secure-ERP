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


def list_transactions_sales():
    transactions_base = data_manager.read_table_from_file(DATAFILE)
    transactions_base.insert(0, HEADERS)
    return transactions_base


def add_transaction_sales(record):
    record.insert(0, util.generate_id())
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
    transactions = data_manager.read_table_from_file(DATAFILE)
    transactions_in_product_revenue = {}

    for transaction in transactions:
        product = transaction[2]
        price = float(transaction[3])
        if product in transactions_in_product_revenue:
            transactions_in_product_revenue[product] += price
        else:
            transactions_in_product_revenue[product] = price

    highest_revenue = 0
    product_with_highest_revenue = None

    for product, revenue in transactions_in_product_revenue.items():
        if revenue > highest_revenue:
            highest_revenue = revenue
            product_with_highest_revenue = product
    return product_with_highest_revenue


def check_user_date(date_1, date_2):
    transactions = data_manager.read_table_from_file(DATAFILE)
    date_format = '%Y-%m-%d'
    date_1_iso = datetime.strptime(date_1, date_format)
    date_2_iso = datetime.strptime(date_2, date_format)

    if date_1_iso < date_2_iso:
        start_date = date_1_iso
        end_date = date_2_iso
    else:
        start_date = date_2_iso
        end_date = date_1_iso
    list_of_date = []

    for transaction in transactions:
        if start_date <= datetime.strptime(transaction[4], "%Y-%m-%d") <= end_date:
            list_of_date.append(transaction[4])
    return list_of_date


def count_transactions_between_sales(date_1, date_2):
    count_transactions_between_dates = check_user_date(date_1, date_2)
    return len(count_transactions_between_dates)


def sum_transactions_between_sales(date_1, date_2):
    transactions = data_manager.read_table_from_file(DATAFILE)
    list_of_dates_between_dates = check_user_date(date_1, date_2)
    list_of_price = []
    for transaction in transactions:
        for date in list_of_dates_between_dates:
            if date == transaction[4]:
                list_of_price.append(float(transaction[3]))
    return sum(list_of_price)
