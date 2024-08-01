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


def get_all():
    """
    Returns an employee's details from a REST API endpoint in JSON format

    Args:
    employee_id(int): Unique employee id

    Return:
    a JSON file
    """
    # Get name, username and to-do list of all employees
    r = f"https://jsonplaceholder.typicode.com/users/"
    try:
        user_response = requests.get(r)
    except requests.execeptions.RequestException:
        return "Conection failed"
    user_json_obj = user_response.json()  # a list of dict
    print(user_json_obj)
    total_employees = len(user_json_obj)
    print(total_employees)
    employee_id = []
    employee_username = []

    r = f"https://jsonplaceholder.typicode.com/todos/"
    try:
        todo_response = requests.get(r)
    except requests.execeptions.RequestException:
        return "Conection failed"
    todo_json_obj = todo_response.json()  # list of dicts also
    print(todo_json_obj)
    total_todos = len(todo_json_obj)
    total_todo_per_employee = int(total_todos / total_employees)
    print(total_todo_per_employee)
    tasks_title = []
    tasks_status = []

    # Iterate through json_obj's and collate info from all employees
    result_dict = {}
    for i in range(total_employees):
        employee_id.append(user_json_obj[i].get('id'))
        employee_username.append(user_json_obj[i].get('username'))
        for j in range(total_todo_per_employee):
            result = []
            for k in range(total_todo_per_employee):
                tasks_title.append(todo_json_obj[k].get('title'))
                tasks_status.append(todo_json_obj[k].get('completed'))
                employee_variables = {
                    "username": employee_username[i],
                    "task": tasks_title[k],
                    "completed": tasks_status[k]
                }
                result.append(employee_variables)
            result_dict.update({employee_id[i]: result})

    # return dict of list values. the lists are a list of dicts
    return result_dict


if __name__ == '__main__':
    json_data = get_all()
    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_data, f)
