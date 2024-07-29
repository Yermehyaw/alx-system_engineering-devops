#!/usr/bin/python3

"""
Modules Imported: requests

requests: make HTTP requests and responses in py script
sys: execute shell commands from py script
"""
import requests
import sys


def get_employee(employee_id):
    """
    Returns an employee's to-do list from a REST API endpoint

    Args:
    employee_id(int): Unique employee id

    Return:
    Employee's to-do list (str)
    """
    try:
        int(employee_id)
    except Exception:
        raise TypeError("Enter a valid argument")

    # Get employee name
    try:
        r = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    except requests.exeception.RequestException:
        return "Conection failed"
    response = requests.get(r)
    json_obj = response.json()  # a dict
    employee_name = json_obj.get('name')  # no need to make an extra var
    print(employee_name)

    # get the to-do list
    r = f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
    with requests.get(r) as response:
        json_obj = response.json()  # list of dicts
        print(json_obj)
        total = len(json_obj)  # only user specific tasks are in response
        tasks_completed = 0
        tasks_title = []
        for i in range(total):
            for key, value in json_obj[i].items():
                # if key and value corresponds to 'completed: true'
                if key == 'completed' and value:
                    tasks_completed += 1
                    tasks_title.append(json_obj[i].get('title'))
    result = (
        f"Employee {employee_name} is done with ({tasks_completed}/{total})"
        + f"\t {tasks_title[0]}"
        + f"\t {tasks_title[1]}"
        )
    print(tasks_title)
    print(result)
    return result


def print_style(list_str):
    """
    Returns formatted text derived from a list

    Args:
    list_str(str): a list of strings

    Return:
    formatted string
    """
    for i in range(len(list_str)):
        return f"\t {list_str[i]}"


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee(employee_id)
