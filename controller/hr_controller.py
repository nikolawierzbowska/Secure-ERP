from model.hr import hr
from view import terminal as view
import datetime

HEADERS = hr.HEADERS


def list_employees():
    view.print_table(hr.list_employees_hr(), HEADERS)


def validate_dates():
    view.print_message("Enter the dates in YYYY-MM-DD format: ")
    while True:
        try:
            date = view.get_input(HEADERS[2])
            if datetime.datetime.strptime(date, '%Y-%m-%d'):
                return date
            else:
                continue
        except ValueError:
            view.print_message("Invalid date format. Please use YYYY-MM-DD format")


def validate_clearance():
    view.print_message("Enter the clearance from 0 to 7: ")
    while True:
        clearance = view.get_input(HEADERS[4])
        if clearance in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            return clearance
        else:
            view.print_message("Invalid clearance ")
            continue


def get_header():
    new_employee = []
    new_employee.append(view.get_input(HEADERS[1]))
    new_employee.append(validate_dates())
    new_employee.append(view.get_input(HEADERS[3]))
    new_employee.append(validate_clearance())
    return new_employee


def add_employee():
    new_employee = get_header()
    hr.add_employee_hr(new_employee)


def get_unique_id_employee():
    id_employee_input = view.get_input(HEADERS[0])
    return id_employee_input


def update_employee():
    id_employee = get_unique_id_employee()
    if not hr.is_employee_existing_hr(id_employee):
        view.print_error_message("ID not found")
        return
    update_employee_info = get_header()
    hr.update_employee_hr(id_employee, update_employee_info)


def delete_employee():
    id_employee = get_unique_id_employee()
    if not hr.is_employee_existing_hr(id_employee):
        view.print_error_message("ID not found")
        return
    hr.delete_employee_hr(id_employee)
    view.print_message(f"Employee {id_employee} has been removed.")


def get_oldest_and_youngest():
    employee1_and_2 = hr.get_oldest_and_youngest_hr()
    view.print_general_results(employee1_and_2, "Oldest and youngest employee")


def get_average_age():
    average_age = hr.get_average_age_hr()
    view.print_general_results(average_age, "The average age of employees")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    number_employees_clearance = hr.count_employees_with_clearance_hr()
    view.print_general_results(number_employees_clearance,
                               "The number of employees who have at least the input clearance level")


def count_employees_per_department():
    number_of_employees_per_department = hr.count_employees_per_department()
    view.print_general_results(number_of_employees_per_department, "The number of employees per department")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
