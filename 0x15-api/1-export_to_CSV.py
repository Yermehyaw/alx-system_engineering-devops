#!/usr/bin/python3

"""
Modules Imported: requests

csv: create csv formatted text
requests: make HTTP requests and responses in py script
sys: execute shell commands from py script
"""
import csv
import requests
import sys


def get_csv(employee_id):
    """
    Returns an employee's details from a REST API endpoint in CSV format

    Args:
    employee_id(int): Unique employee id

    Return:
    a CSV file
    """
    try:
        int(employee_id)
    except Exception:
        raise TypeError("Enter a valid argument")

    # Get employee name and username
    try:
        r = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    except requests.execeptions.RequestException:
        return "Conection failed"
    response = requests.get(r)
    json_obj = response.json()  # a dict
    employee_name = json_obj.get('name')
    employee_username = json_obj.get('username')

    # get the to-do list
    r = f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
    with requests.get(r) as response:
        json_obj = response.json()  # list of dicts
        print(json_obj)
        tasks_title = []
        tasks_status = []
        total = len(json_obj)  # only user specific tasks are in response
        for i in range(total):
            tasks_status.append(json_obj[i].get('completed'))
            tasks_title.append(json_obj[i].get('title'))

    # Get employee details in csv
    result = []
    rows = total

    for i in range(rows):  # different values of tasks_title to append to list
        employee_variables = [
            f'"{employee_id}"',
            f'"{employee_username}"',
            f'"{tasks_status[i]}"',
            f'"{tasks_title[i]}"'
        ]
        result.append(employee_variables)
    return result


if __name__ == '__main__':
    employee_id = sys.argv[1]
    csv_data = get_csv(employee_id)  # csv is a list of lists
    with open(f'{employee_id}.csv', 'w', newline='') as f:
        write_into = csv.writer(
            f,
            quoting=csv.QUOTE_MINIMAL,
            quotechar="'",
            delimiter=','
        )
        write_into.writerows(csv_data)
