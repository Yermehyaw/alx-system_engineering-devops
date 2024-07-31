#!/usr/bin/python3

"""
Modules Imported: requests

csv: create csv formatted text
requests: make HTTP requests and responses in py script
subprocess: execute shell commands from py script
sys: execute shell commands from py script
"""
import csv
import requests
import subprocess
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

    # Get employee name abd username
    try:
        r = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    except requests.execeptions.RequestException:
        return "Conection failed"
    response = requests.get(r)
    json_obj = response.json()  # a dict
    employee_name = json_obj.get('name')
    employee_username = json_obj.get['usernane']

    # get the to-do list
    r = f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
    with requests.get(r) as response:
        json_obj = response.json()  # list of dicts
        print(json_obj)
        total = len(json_obj)  # only user specific tasks are in response
 #       tasks_completed = 0
        tasks_title = []
        for i in range(total):
            for key, value in json_obj[i].items():
                # if key and value corresponds to 'completed: true'
                if key == 'completed':
#                    tasks_completed += 1
                    task_status = value
                    tasks_title.append(json_obj[i].get('title'))  # list of dict
#    for i in range(tasks_completed):
#        print(f"\t {tasks_title[i]}")


# Get employee details in csv
    result = [[]]
    for i in range(total):
        result = result[0].append(f'"{employee_id}",
                            "{employee_username}",
                            "{str(task_status)}",
                            "{task_title[i]}"'
                )
    return result



if __name__ == '__main__':
    employee_id = sys.argv[1]
    csv_data = get_csv(employee_id)  # csv is a list of lists

    create_csv_cmd = f'touch {employee_id}.csv'
    try:
        subprocess.run(create_csv_cmd, shell=True, check=True)
    except CalledProcessError:
        print('Couldnt create csv file')

    with open(f'{employee_id}.csv', 'w', newline='') as f:
        write_in = csv.write(f)
        write_in.write(csv_data)
