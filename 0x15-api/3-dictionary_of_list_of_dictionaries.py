#!/usr/bin/python3

"""
Modules Imported: requests

json: create json formatted text/files
requests: make HTTP requests and responses in py script
sys: execute shell commands from py script
"""
import json
import requests
import sys


def get_all(employee_id):
    """
    Returns an employee's details from a REST API endpoint in JSON format

    Args:
    employee_id(int): Unique employee id

    Return:
    a JSON file
    """
    # Get name and username of all employees
    try:
        r = f"https://jsonplaceholder.typicode.com/users/"
    except requests.execeptions.RequestException:
        return "Conection failed"
    response = requests.get(r)
    json_obj = response.json()  # a list of dict
    total_employees = len(json_obj)
    employee_name = []
    employee_username = []
    for i in range(total_employees):
        employee_name.append(json_obj[i].get('name'))
        employee_username.append(json_obj[i].get('username'))

    # get to-do list of all employees
    r = f"https://jsonplaceholder.typicode.com/todos/"
    with requests.get(r) as response:
        json_obj = response.json()  # list of dicts
        print(json_obj)
        tasks_title = []
        tasks_status = []
        total = len(json_obj)
        for i in range(total):
            tasks_status.append(json_obj[i].get('completed'))
            tasks_title.append(json_obj[i].get('title'))

    # Get employee details in a dict with a list as its value
    result = []
    result_dict = {employee_id: result}
    rows = total

    for i in range(rows):  # different values of tasks_title to append to list
        employee_variables = {
            "username": employee_username,
            "task": tasks_title[i],
            "completed": tasks_status[i]
        }
        result.append(employee_variables)

    for i in 
    return result_dict


if __name__ == '__main__':
    employee_id = sys.argv[1]
    json_data = get_json(employee_id)
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(json_data, f)
