#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_data = {}
    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        todos = response.json()

        all_data[user_id] = [{"username": username,
                              "task": todo["title"],
                              "completed": todo["completed"]} for todo in todos]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
