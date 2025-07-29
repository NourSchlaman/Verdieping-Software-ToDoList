import random
import time

import data
from functions.functions import false_user_number_input, auto_increment_id, progress_bar, save_tasks_to_file


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


