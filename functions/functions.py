import json
import random
import time
from pathlib import Path

import data
import os
from tqdm import tqdm

def setup():
    data.downloadPath = get_downloads_folder()
    data.filePathJson = data.downloadPath / "todo_data.json"
    data.filePathTxt = data.downloadPath / "todo_export.txt"
    if data.filePathJson.exists():
        load_tasks()

def load_tasks():
    with open(data.filePathJson, "r") as file:
        data.tasks = json.load(file)

def get_downloads_folder():
    if os.name == "nt":
        return Path(os.environ["USERPROFILE"]) / 'Downloads'
    else:
        return Path.home() / 'Downloads'

def save_tasks_to_file():
        with open(data.filePathJson, "w") as file:
            json.dump(data.tasks, file, indent=4)

def progress_bar(range_value, function="Processing"):
    end = random.randint(5, range_value)

    for i in tqdm(range(end), desc=function, bar_format="{l_bar}{bar}"):
        time.sleep(.5)

def false_user_input():
    notCorrectDecisionQuip = random.choice(data.notCorrectDecisionQuips)
    time.sleep(1.5)
    print(notCorrectDecisionQuip["text-reaction"])
    time.sleep(1.5)
    print(notCorrectDecisionQuip["text-retry"])
    time.sleep(1.5)

def false_user_number_input(user_input, min_value, max_value):
    if not user_input.isdigit() or int(user_input) > max_value or int(user_input) < min_value:
        false_user_input()
        return True
    else:
        return False


def false_user_yes_no_input(user_input):
    if user_input.lower() not in ["yes", "no"]:
        false_user_input()
        return True
    else:
        return False

def false_id(task_id):
    if not task_id.isdigit() or not check_if_task_exists(int(task_id)):
        false_user_input()
        return True
    else:
        return False

def auto_increment_id():
    return data.tasks[-1]["id"] + 1 if data.tasks else 1

def check_if_task_exists(task_id):
    return any(task["id"] == task_id for task in data.tasks)

def get_id_array():
    return [task["id"] for task in data.tasks]

def get_task_by_id(task_id):
    for task in data.tasks:
        if task["id"] == task_id:
            return task
    return None




