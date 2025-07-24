import random
import time
import data
from tqdm import tqdm

from data import savingTaskQuips


def view_tasks():
    data.tasks.sort(key=lambda task: task["priority"], reverse=True)
    print("Here are your tasks:")
    for task in data.tasks:
        print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}")
        time.sleep(.15)

def add_task():
    validPriority = False
    taskPrio = 1
    print(random.choice(data.creatingTaskQuips)["text"])
    time.sleep(1.5)
    taskName = input("What should the task be called? -> ")
    creatingTaskNamePriorityQuip = random.choice(data.creatingTaskNamePriorityQuips)
    time.sleep(2)
    print(creatingTaskNamePriorityQuip["text-greeting"] + taskName + creatingTaskNamePriorityQuip["text-reaction"])
    time.sleep(2)
    while not validPriority:
        taskPrio = input(creatingTaskNamePriorityQuip["text-prio"])
        if false_user_number_input(taskPrio, 1, 10) :
            continue
        else:
            validPriority = True

    if validPriority is True:
        newTask = {"id": auto_increment_id(), "name": taskName, "priority": int(taskPrio)}
        time.sleep(2)
        print("\n")
        print("Your new task will be: ")
        print(f"ID: {newTask['id']}, Name: {newTask['name']}, Priority: {newTask['priority']}")
        time.sleep(1)

        savingTaskQuip = random.choice(data.savingTaskQuips)
        print(savingTaskQuip["text"])
        time.sleep(.15)
        progress_bar(savingTaskQuip["timer"], "Saving")
        data.tasks.append(newTask)



def remove_task():
    print("Removing task...")

def exit_app():
    print("Exiting...")

def progress_bar(range_value, function="Processing"):
    end = random.randint(5, range_value)

    for i in tqdm(range(end), desc=function, bar_format="{l_bar}{bar}"):
        time.sleep(1.5)


def false_user_number_input(user_input, min_value, max_value):
    if not user_input.isdigit() or int(user_input) > max_value or int(user_input) < min_value:
        notCorrectDecisionQuip = random.choice(data.notCorrectDecisionQuips)
        time.sleep(1.5)
        print(notCorrectDecisionQuip["text-reaction"])
        time.sleep(1.5)
        print(notCorrectDecisionQuip["text-retry"])
        time.sleep(1.5)
        return True
    else:
        return False

def auto_increment_id():
    return data.tasks[-1]["id"] + 1 if data.tasks else 1

