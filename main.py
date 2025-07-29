import random
import time
import data
from functions import functions
from functions.functionalities.add_task import add_task
from functions.functionalities.exit_app import exit_app
from functions.functionalities.export_tasks import export_tasks
from functions.functionalities.remove_task import remove_task
from functions.functionalities.view_tasks import view_tasks

actions = {
    1: view_tasks,
    2: add_task,
    3: remove_task,
    4: export_tasks,
    5: exit_app
}

if __name__ == "__main__":

    functions.setup()
# This is the welcome message, and the list options
    print("Welcome to your To-Do list Task Manager Tool")

    time.sleep(1)
    while True:
        print("What would you like to do?")
        time.sleep(0.8)
        print("==========================")
        time.sleep(0.3)
        print("1. View tasks")
        time.sleep(0.3)
        print("2. Add a task")
        time.sleep(0.3)
        print("3. Remove a task")
        time.sleep(0.3)
        print("4. Export tasks")
        time.sleep(0.3)
        print("5. Exit the application")
        time.sleep(0.3)
        print("==========================")
        time.sleep(0.3)

# The user can make a decision, and the program will process it
        decision1 = input("Please enter your choice (1-5): ")
        if random.choice([True, False, False]):
            time.sleep(1)
            processingQuip = random.choice(data.processingQuips)
            print(processingQuip["text"])
            time.sleep(1)
            functions.progress_bar(processingQuip["timer"])


# The program will check if the decision is valid, and if not, it will give a quip about it and make the user retry
        if functions.false_user_number_input(decision1, 1, 5) :
            continue

# After processing, the program will give a quip about the decision made
        decision1 = int(decision1)
        decisionMakingQuip = random.choice(data.decisionMakingQuips)
        time.sleep(2)
        print(decisionMakingQuip["text"])
        time.sleep(1)
# If the program decides that the decision is not valid, it will make the user retry
        if decisionMakingQuip["retry"]:
            print("\n")
            continue
# If that is not the case, it will execute the action
        print("Your decision is", data.actionOptions[decision1 - 1])

        time.sleep(2)
        action = actions.get(decision1)
        if action:
            print("\n")
            time.sleep(.8)
            print("==========================")
            action()
            time.sleep(.8)
            print("==========================")

# When the action is done, the program will ask if the user wants to do something else
        print("\n")
        decision2 = input("Would you like to do something else? (yes/no): ")
        if decision2 == "yes":
            time.sleep(1)
            continue
        else:
            exit()








