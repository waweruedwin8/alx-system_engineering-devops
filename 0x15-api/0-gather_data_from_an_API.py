#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This script fetches and displays TODO list progress for a given employee ID
from a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get("completed")]

    number_of_done_tasks = len(done_tasks)

    # Output the results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
