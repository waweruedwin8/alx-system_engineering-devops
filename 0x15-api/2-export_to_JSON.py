#!/usr/bin/python3
"""
2-export_to_JSON.py

This script fetches and exports TODO list progress for a given employee ID
from a REST API in JSON format.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data and TODO list progress from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee username and a list of tasks.
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

    return user_data['username'], todos_data


def export_to_json(employee_id, username, todos):
    """
    Exports the TODO list progress to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        username (str): The username of the employee.
        todos (list): A list of tasks.
    """
    filename = f"{employee_id}.json"
    data = {str(employee_id): [{"task": todo['title'], "completed": todo['completed'], "username": username} for todo in todos]}
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    username, todos = fetch_employee_data(employee_id)
    export_to_json(employee_id, username, todos)
