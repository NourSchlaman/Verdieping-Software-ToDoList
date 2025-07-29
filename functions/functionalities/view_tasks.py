import time

import data


def view_tasks():
    if data.tasks:
        data.tasks.sort(key=lambda task: task["priority"], reverse=True)
        print("Here are your tasks:")
        time.sleep(.5)
        for task in data.tasks:
            print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}")
            time.sleep(.3)
    else:
        print("No tasks found.")
