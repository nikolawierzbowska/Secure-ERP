""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

data_base = data_manager.read_table_from_file(DATAFILE)


def list_customers_crm():
    data_base.insert(0, HEADERS)
    return data_base


def create_customers_crm(table, record):
    record.insert(0, util.generate_id())
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, ";")


