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




def list_customers_crm():
    data_base = data_manager.read_table_from_file(DATAFILE)
    data_base.insert(0, HEADERS)
    return data_base


def create_customers_crm( record):
    record.insert(0, util.generate_id())
    update_list_of_customer = data_manager.read_table_from_file(DATAFILE)
    update_list_of_customer.append(record)
    data_manager.write_table_to_file(DATAFILE, update_list_of_customer)


def is_customer_exist_crm(id_customer):
    customers = data_manager.read_table_from_file(DATAFILE)
    for customer in customers:
        if id_customer == customer[0]:
            return True
    return False


def update_customer_crm(id_customer, customer_data):
    customers = data_manager.read_table_from_file(DATAFILE)
    for index, customer in enumerate(customers):
        if id_customer == customer[0]:
            del customers[index]
            customers.insert(index, [id_customer, *customer_data])
    data_manager.write_table_to_file(DATAFILE, customers)



def delete_customer_crm(id_customer):
    customers = data_manager.read_table_from_file(DATAFILE)
    for index, customer in enumerate(customers):
        if id_customer == customer[0]:
            del customers[index]
    data_manager.write_table_to_file(DATAFILE, customers)


def get_subscribed_emails_crm():
    pass