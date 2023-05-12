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

data_base = data_manager.read_table_from_file(DATAFILE)


def list_transactions_sales():
    data_base.insert(0, HEADERS)
    return data_base

def add_transaction_sales(table, record):
    record.insert(0, util.generate_id())
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, ";")
