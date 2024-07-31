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
    r = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    try:
        response = requests.get(r)
    except requests.exceptions.RequestException:
        return "Conection failed"
    json_obj = response.json()  # a dict
    employee_name = json_obj.get('name')  # no need to make an extra var

    # get the to-do list
    r = f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
    with requests.get(r) as response:
        json_obj = response.json()  # list of dicts
        total = len(json_obj)  # only user specific tasks are in response
        tasks_completed = 0
        tasks_title = []
        for i in range(total):
            for key, value in json_obj[i].items():
                # if key and value corresponds to 'completed: true'
                if key == 'completed' and value:
                    tasks_completed += 1
                    tasks_title.append(json_obj[i].get('title'))
    result = (f"Employee {employee_name} is done with \
tasks({tasks_completed}/{total}):")
    print(result)
    for i in range(tasks_completed):
        print(f"\t {tasks_title[i]}")
    return result


if __name__ == "__main__":
    employee_id = sys.argv[1]
#    employee_id = 1  # for mobile testing
    get_employee(employee_id)
