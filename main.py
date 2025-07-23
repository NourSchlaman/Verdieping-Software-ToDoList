import random
import time
from tqdm import tqdm
import functions
import data

actions = {
    "1": functions.view_tasks,
    "2": functions.add_task,
    "3": functions.remove_task,
    "4": functions.exit_app
}

if __name__ == "__main__":

# This is the welcome message, and the list options
    print("Welcome to your To-Do list Task Manager Tool")
    time.sleep(1)
    while True:
        print("What would you like to do?")
        time.sleep(0.5)
        print("========================================")
        time.sleep(0.5)
        print("1. View tasks")
        time.sleep(0.5)
        print("2. Add a task")
        time.sleep(0.5)
        print("3. Remove a task")
        time.sleep(0.5)
        print("4. Exit")
        time.sleep(0.5)

# The user can make a decision, and the program will process it
        decision = input("Please enter your choice (1-4): ")
        time.sleep(1)
        processingQuip = random.choice(data.processingQuips)
        print(processingQuip["text"])
        functions.progress_bar(processingQuip["timer"])
# After processing, the program will give a quip about the decision made
        decisionMakingQuip = random.choice(data.decisionMakingQuips)
        time.sleep(2)
        print(decisionMakingQuip["text"])
        time.sleep(2)
# If the program decides that the decision is not valid, it will make the user retry
        if decisionMakingQuip["retry"]:
            continue
# If that is not the case, it will execute the action
        print("Your decision is :", decision)
        time.sleep(2)
        action = actions.get(decision)
        if action:
            action()








