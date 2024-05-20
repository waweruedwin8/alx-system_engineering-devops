#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This script fetches and displays TODO list progress for a given employee ID
from a REST API.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data and TODO list progress from the REST API.
    
    Args:
    employee_id (int): The ID of the employee.
    
    Returns:
    tuple: A tuple containing the employee name and a list of tasks.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data.get("name"), todos_data


def display_employee_todo_progress(employee_name, todos):
    """
    Displays the employee's TODO list progress.
    
    Args:
    employee_name (str): The name of the employee.
    todos (list): A list of tasks.
    """
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_name, todos = fetch_employee_data(employee_id)
    display_employee_todo_progress(employee_name, todos)
