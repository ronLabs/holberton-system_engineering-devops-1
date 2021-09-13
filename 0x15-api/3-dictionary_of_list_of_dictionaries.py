#!/usr/bin/python3
"""This module makes a request to an API
and exports the results to a json file"""
import json
from sys import argv
import requests as rq

url = 'https://jsonplaceholder.typicode.com/{}'
if __name__ == '__main__':
    users = rq.get(url.format('users')).json()
    todos = rq.get(url.format('todos')).json()

    data = dict()
    for u in users:
        _id = u['id']
        data[_id] = []
        for t in todos:
            task = {'task': t['title'],
                    'username': u['username'],
                    'completed': t['completed']}
            data[_id].append(task)

    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
