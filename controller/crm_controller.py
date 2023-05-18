from model.crm import crm
from view import terminal as view

HEADERS = crm.HEADERS


def list_customers():
    view.print_table(crm.list_customers_crm(), HEADERS)


def validate_subscription():
    view.print_message("Enter the subscription status 0 or 1: ")
    while True:
        subscription = view.get_input(HEADERS[3])
        if subscription in ["0", "1"]:
            return subscription
        else:
            view.print_message("Invalid subscription status ")
            continue


def get_information_about_customer():
    new_customer = [view.get_input(HEADERS[1]), view.get_input(HEADERS[2]), validate_subscription()]
    return new_customer


def add_customer():
    new_customer = get_information_about_customer()
    crm.create_customers_crm(new_customer)
    view.print_message(f"Customer {new_customer} has been added.")


def get_unique_id():
    id_customer_input = view.get_input(HEADERS[0])
    return id_customer_input


def update_customer():
    view.print_table(crm.list_customers_crm(), HEADERS)
    id_customer = get_unique_id()
    if not crm.is_customer_existing_crm(id_customer):
        view.print_error_message("ID not found")
        return
    update_customer_info = get_information_about_customer()
    crm.update_customer_crm(id_customer, update_customer_info)
    view.print_message(f"Customer {id_customer} has been updated.")


def delete_customer():
    view.print_table(crm.list_customers_crm(), HEADERS)
    id_customer = get_unique_id()
    if not crm.is_customer_existing_crm(id_customer):
        view.print_error_message("ID not found")
        return
    crm.delete_customer_crm(id_customer)
    view.print_message(f"Customer {id_customer} has been removed.")


def get_subscribed_emails():
    subscribed_emails = crm.get_subscribed_emails_crm()
    if not subscribed_emails:
        view.print_error_message("No active subscription found")
    else:
        view.print_general_results(subscribed_emails, "The emails of subscribed customers")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
