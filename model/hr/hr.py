""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
#from datetime import datetime

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


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
def get_oldest_and_youngest_hr():
    employees = data_manager.read_table_from_file(DATAFILE)
    persons_dates_1 = []
    for employee in employees:
        person_date_int = int(employee[2][0:4])
        person_month_int = int(employee[2][5:7])
        person_day_int = int(employee[2][8:10])
        personsdates = [person_date_int, person_month_int, person_day_int]
        persons_dates_1.append(personsdates)
    print(persons_dates_1)
    print(max(persons_dates_1))
    print(min(persons_dates_1))
