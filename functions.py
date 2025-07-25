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


def export_tasks_to_txt():
        data.tasks.sort(key=lambda task: task["priority"], reverse=True)
        with open(data.filePathTxt, "w") as file:
            for task in data.tasks:
                file.write(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}\n")


def export_tasks():
    data.filePathJson = Path(data.filePathJson)
    if data.filePathJson.exists():
        exportingTasksQuip = random.choice(data.exportingTasksQuips)
        print(exportingTasksQuip["text"])
        progress_bar(exportingTasksQuip["timer"], "Exporting")
        time.sleep(1.5)
        export_tasks_to_txt()
        print("Export complete.")
        time.sleep(1.5)
        print(f"Tasks have been exported to {data.filePathTxt}")
        time.sleep(1.5)
    else:
        print("No tasks to export")

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

def add_task():
    validPriority = False
    time.sleep(1)
    print(random.choice(data.creatingTaskQuips)["text"])
    time.sleep(1.5)
    taskName = input("What should the task be called? -> ")
    creatingTaskNamePriorityQuip = random.choice(data.creatingTaskNamePriorityQuips)
    time.sleep(1.5)
    print(creatingTaskNamePriorityQuip["text-greeting"] + taskName + creatingTaskNamePriorityQuip["text-reaction"])
    time.sleep(1)
    while not validPriority:
        taskPrio = input(creatingTaskNamePriorityQuip["text-prio"])
        if false_user_number_input(taskPrio, 1, 10) :
            continue
        else:
            validPriority = True

    if validPriority is True:
        newTask = {"id": auto_increment_id(), "name": taskName, "priority": int(taskPrio)}
        time.sleep(1)
        print("\n")
        print("Your new task will be: ")
        time.sleep(1)
        print(f"ID: {newTask['id']}, Name: {newTask['name']}, Priority: {newTask['priority']}")
        time.sleep(1)

        savingTaskQuip = random.choice(data.savingTaskQuips)
        print(savingTaskQuip["text"])
        time.sleep(.15)
        progress_bar(savingTaskQuip["timer"], "Saving")
        data.tasks.append(newTask)
        save_tasks_to_file()



def remove_task():
    validId = False
    print(random.choice(data.deleteTaskQuips))
    time.sleep(1)
    view_tasks()
    time.sleep(.5)
    while not validId:
        toBeDeleted = input(random.choice(data.deleteQuestionQuips) + " (Enter ID) -> ")
        if false_id(toBeDeleted):
            continue
        else:
            validId = True

    task = get_task_by_id(int(toBeDeleted))
    time.sleep(1)
    print("You are about to delete the following task:")
    time.sleep(.5)
    print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}")
    time.sleep(1)

    delete_conformation(task)




def exit_app():
    print("Exiting...")
    exit()

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


def delete_conformation(task):
    isValid = False
    absolutelyCounter = 0
    randomRange = 100
    while not isValid:
        isHeSure = input("Are you" + " absolutely" * absolutelyCounter + " sure? (yes/no) -> ")
        if false_user_yes_no_input(isHeSure):
            continue
        else:
            if isHeSure.lower() == "yes":
                number = random.randint(1, randomRange)
                if number > 45:
                    absolutelyCounter += 1
                    randomRange += 10
                    continue
                else:

                    print(data.deletingTaskQuips[min(absolutelyCounter, len(data.deletingTaskQuips) - 1)])
                    data.tasks.remove(task)
                    isValid = True
            else:
                print(data.notDeleteTaskQuips[min(absolutelyCounter, len(data.notDeleteTaskQuips) - 1)])
                isValid = True

