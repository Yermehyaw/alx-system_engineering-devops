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


def get_json(employee_id):
    """
    Returns an employee's details from a REST API endpoint in JSON format

    Args:
    employee_id(int): Unique employee id

    Return:
    a JSON file
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
    return result_dict


if __name__ == '__main__':
    employee_id = sys.argv[1]
    json_data = get_json(employee_id)
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(json_data, f)
