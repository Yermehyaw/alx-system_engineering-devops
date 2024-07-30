#!/usr/bin/python3

"""
Modules Imported: requests

requests: make HTTP requests and responses in py script
sys: execute shell commands from py script
"""
import requests
import sys


def get_cv(employee_id):
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
    result = (f"Employee {employee_name} is done with\
            ({tasks_completed}/{total})")
    print(result)
    for i in range(tasks_completed):
        print(f"\t {tasks_title[i]}")
    print(tasks_title)
    return result


# Get employee details in csv
r = f'https://jsonplaceholder.typicode.com/todos/?userId={employee_id}'
with requests.get(r) as response:
    json_obj = response.json()

    result = []
    for i in range():
        result = result.append(f'"{employee_id}", 
                            "{username}", 
                            "{task_status}", 
                            "{task_title[i]}"'
                )



if __name__ == '__main__':
    employee_id = sys.argv[1]
    csv = get_csv(employee_id)  # csv is a list
    sys.cmd('touch {employee_id}.csv')
    with open(f'{employee_id}.csv') as f:
        f.write(str(csv))
