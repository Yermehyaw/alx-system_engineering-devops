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
        total = len(json_obj)  # only user specific tasks are in response
        tasks_title = []
        for i in range(total):
            for key, value in json_obj[i].items():
                # if key and value corresponds to 'completed: true'
                if key == 'completed':
                    task_status = str(value)
                    tasks_title.append(json_obj[i].get('title'))

    # Get employee details in csv
    result = []
    rows = total
    cols = 4  # only employee_id, username, status and title is used

    for i in range(rows):  # different values of tasks_title to append to list
        employee_variables = [
            employee_id,
            employee_username,
            task_status,
            tasks_title[i]
        ]
        print(employee_variables)
        result.append(employee_variables)
    print(result)
    return result


if __name__ == '__main__':
    employee_id = sys.argv[1]
    csv_data = get_csv(employee_id)  # csv is a list of lists
    with open(f'{employee_id}.csv', 'w', newline='') as f:
        write_into = csv.writer(f, quotechar='"', delimiter=',')
        write_into.writerows(csv_data)
