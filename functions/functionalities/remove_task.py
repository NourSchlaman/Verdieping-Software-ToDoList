import random
import time

import data
from functions.functionalities.view_tasks import view_tasks
from functions.functions import false_id, get_task_by_id, false_user_yes_no_input


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