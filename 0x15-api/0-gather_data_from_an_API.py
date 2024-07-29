#!/usr/bin/python3

"""
Modules Imported: requests

requests: make HTTP requests and responses in py script
"""
import requests


def get_employee(employee_id):
    """
    Returns an employee's to-do list from a REST API endpoint

    Args:
    employee_id(int): Unique employee id

    Return:
    Employee's to-do list (str)
    """
    # Get response title
    req = f"https://jsonplaceholder.typicode.com/todos/{employee_id}"
    response = requests.get(req)
    task_title = response.get('title')

    # Get Employee name
    req =  f"https://jsonplaceholder.typicode.com/posts/{employee_id}"
    employee_name = response.get(name)
    tasks_completed = response.get('')
    total_tasks = response.get()

    return f""

if __name__ == "__main__":
    get_employee()
