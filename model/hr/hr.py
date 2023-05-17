""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees_hr():
    employees_base = data_manager.read_table_from_file(DATAFILE)
    employees_base.insert(0,HEADERS)
    return employees_base


def add_employee_hr(record):
    employees_base = data_manager.read_table_from_file(DATAFILE)
    record.insert(0,util.generate_id(employees_base))
    update_list_of_employees = data_manager.read_table_from_file(DATAFILE)
    update_list_of_employees.append(record)
    data_manager.write_table_to_file(DATAFILE, update_list_of_employees)


def is_employee_existing_hr(id_employee):
    employees = data_manager.read_table_from_file(DATAFILE)
    for employee in employees:
        if id_employee == employee[0]:
            return True
    return False


def update_employee_hr(id_employee,employee_data):
    employees = data_manager.read_table_from_file(DATAFILE)
    for index, employee in enumerate(employees):
        if id_employee == employee[0]:
            del employees[index]
            employees.insert(index, [id_employee, *employee_data])
    data_manager.write_table_to_file(DATAFILE,employees)


def delete_employee_hr(id_employee):
    employees = data_manager.read_table_from_file(DATAFILE)
    for index , employee in enumerate(employees):
        if id_employee == employee[0]:
            del employees[index]
    data_manager.write_table_to_file(DATAFILE,employees)


def get_oldest_and_youngest():
    pass

# def min_max():
#     employees = data_manager.read_table_from_file(DATAFILE)
#     date_format = '%Y-%m-%d'
#     birth_dates = []
#     for employee in employees:
#         birth_date = employee[2]
#         birth_dates.append(birth_date)
#     birth_dates = [datetime.strptime(date, date_format) for date in birth_dates]
#     youngest_employee = max(birth_dates)
#     oldest_employee = min(birth_dates)
#     return youngest_employee, oldest_employee
# [11:21 PM]
# to jest ten zakomentowany z którego chyba ostatecznie nie korzystamy
# [11:21 PM]
# działa tylko przy imporcie datetime
# [11:22 PM]
# def get_oldest_and_youngest_hr():
#     employees = data_manager.read_table_from_file(DATAFILE)
#     persons_dates_1 = []
#     for employee in employees:
#         person_date_int = int(employee[2][0:4])
#         person_month_int = int(employee[2][5:7])
#         person_day_int = int(employee[2][8:10])
#         personsdates = [person_date_int, person_month_int, person_day_int]
#         persons_dates_1.append(personsdates)
#     print(persons_dates_1)
#     print(max(persons_dates_1))
#     print(min(persons_dates_1))



def get_average_age_hr():
    employees = data_manager.read_table_from_file(DATAFILE)
    list_of_years = []
    for employee in employees:
        list_of_years.append(int(employee[2][0:4]))
    sum_age_employees =0
    current_year = 2023
    for year in list_of_years:
        age_employee = current_year -year
        sum_age_employees +=age_employee
    average_age_of_employees =sum_age_employees/(len(list_of_years))
    return  average_age_of_employees


def next_birthdays_hr():
    pass


def count_employees_with_clearance_hr():
    pass


def count_employees_per_department():
    pass