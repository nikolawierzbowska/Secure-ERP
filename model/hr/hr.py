""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import datetime
from datetime import timedelta

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees_hr():
    employees_base = data_manager.read_table_from_file(DATAFILE)
    employees_base.insert(0, HEADERS)
    return employees_base


def add_employee_hr(record):
    record.insert(0, util.generate_id())
    update_list_of_employees = data_manager.read_table_from_file(DATAFILE)
    update_list_of_employees.append(record)
    data_manager.write_table_to_file(DATAFILE, update_list_of_employees)


def is_employee_existing_hr(id_employee):
    employees = data_manager.read_table_from_file(DATAFILE)
    for employee in employees:
        if id_employee == employee[0]:
            return True
    return False


def update_employee_hr(id_employee, employee_data):
    employees = data_manager.read_table_from_file(DATAFILE)
    for index, employee in enumerate(employees):
        if id_employee == employee[0]:
            del employees[index]
            employees.insert(index, [id_employee, *employee_data])
    data_manager.write_table_to_file(DATAFILE, employees)


def delete_employee_hr(id_employee):
    employees = data_manager.read_table_from_file(DATAFILE)
    for index, employee in enumerate(employees):
        if id_employee == employee[0]:
            del employees[index]
    data_manager.write_table_to_file(DATAFILE, employees)


def get_oldest_and_youngest_hr():
    employees = data_manager.read_table_from_file(DATAFILE)
    list_of_dates = []
    for employee in employees:
        dates = employee[2].replace("-", "")
        list_of_dates.append(int(dates))
    list_of_names_y = None
    list_of_names_o = None
    for index, employee in enumerate(employees):
        if list_of_dates.index(min(list_of_dates)) == index:
            list_of_names_o = employee[1]
        elif list_of_dates.index(max(list_of_dates)) == index:
            list_of_names_y = employee[1]
    names = list_of_names_o, list_of_names_y
    return tuple(names)


def get_average_age_hr():
    employees = data_manager.read_table_from_file(DATAFILE)
    list_of_years = []
    for employee in employees:
        list_of_years.append(int(employee[2][0:4]))
    sum_age_employees = 0
    current_year = 2023
    for year in list_of_years:
        age_employee = current_year - year
        sum_age_employees += age_employee
    average_age_of_employees = int(sum_age_employees / (len(list_of_years)))
    return average_age_of_employees


def next_birthdays_hr(get_dates):
    employees = data_manager.read_table_from_file(DATAFILE)
    start_date = datetime.strptime(get_dates, "%Y-%m-%d")
    end_date = start_date + timedelta(days=14)

    list_of_names = []
    for employee in employees:
        if start_date <= datetime.strptime(employee[2], "%Y-%m-%d") <= end_date:
            list_of_names.append(employee[1])
    return list_of_names


def count_employees_with_clearance_hr(get_clearance):
    employees = data_manager.read_table_from_file(DATAFILE)
    list_of_clearance = []
    for employee in employees:
        if get_clearance <= employee[4]:
            list_of_clearance.append(employee[4])
    return len(list_of_clearance)


def count_employees_per_department():
    employees = data_manager.read_table_from_file(DATAFILE)
    number_of_employees_per_department = {}
    for employee in employees:
        department = employee[3]
        if department in number_of_employees_per_department:
            number_of_employees_per_department[department] += 1
        else:
            number_of_employees_per_department[department] = 1
    return number_of_employees_per_department
