import random
import time
from tqdm import tqdm
import functions
import data

actions = {
    1: functions.view_tasks,
    2: functions.add_task,
    3: functions.remove_task,
    4: functions.exit_app
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
        print("4. Exit")
        time.sleep(0.3)

# The user can make a decision, and the program will process it
        decision1 = input("Please enter your choice (1-4): ")
        time.sleep(1)
        processingQuip = random.choice(data.processingQuips)
        print(processingQuip["text"])
        if random.choice([True, False]):
            functions.progress_bar(processingQuip["timer"])


# The program will check if the decision is valid, and if not, it will give a quip about it and make the user  retry
        if functions.false_user_number_input(decision1, 1, 4) :
            continue

# After processing, the program will give a quip about the decision made
        decision1 = int(decision1)
        decisionMakingQuip = random.choice(data.decisionMakingQuips)
        time.sleep(2)
        print(decisionMakingQuip["text"])
        time.sleep(2)
# If the program decides that the decision is not valid, it will make the user retry
        if decisionMakingQuip["retry"]:
            print("\n")
            continue
# If that is not the case, it will execute the action
        print("Your decision is", data.actionOptions[decision1 - 1])

        time.sleep(2)
        print("\n")
        action = actions.get(decision1)
        if action:
            action()
# When the action is done, the program will ask if the user wants to do something else
        print("\n")
        decision2 = input("Would you like to do something else? (yes/no): ")
        if decision2 == "yes":
            continue
        else:
            exit()








