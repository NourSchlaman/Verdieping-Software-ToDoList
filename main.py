import random
import time
from tqdm import tqdm

tasks = [
    {"id":1 ,"name": "1000 pushups", "priority": 8},
    {"id":2 ,"name": "Heel veel aardbeien eten", "priority": 3},
    {"id":3 ,"name": "afvallen", "priority": 10},
]

decisionMakingQuips = [
    {"text": "Thank you for your Critical Decision Making", "retry": False},
    {"text": "You thought long and hard about that decision", "retry": False},
    {"text": "Are you sure about that?", "retry": False},
    {"text": "Hmmmm, interesting choice", "retry": False},
    {"text": "You must have given that a lot of thought", "retry": False},
    {"text": "I wouldn't have made that choice", "retry": False},
    {"text": "NOOO PLEASE NOT THAT ONE", "retry": True},
    {"text": "Sorry for the inconvenience, but that choice is not available at the moment", "retry": True},
    {"text": "ERROR - Something went wrong", "retry": True}
]

processingQuips = [
    {"text": "Processing...", "timer": 10},
    {"text": "Lemme think about that one...", "timer": 20},
    {"text": "Hhmmm, this won't take long...", "timer": 100},
    {"text": "I'm thinking, one moment please...", "timer": 18},
    {"text": "Thinking...", "timer": 20},
    {"text": "Phoe Tough one", "timer": 500}
]

def view_tasks():
    print("Here are your tasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}")
        time.sleep(.15)

def add_task():
    print("Adding task...")

def remove_task():
    print("Removing task...")

def exit_app():
    print("Exiting...")

actions = {
    "1": view_tasks,
    "2": add_task,
    "3": remove_task,
    "4": exit_app
}


def progress_bar(range_value):
    end = random.randint(5, range_value)

    for i in tqdm(range(end), desc="Processing", bar_format="{l_bar}{bar}"):
        time.sleep(1)


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

    decision = input("Please enter your choice (1-4): ")
    time.sleep(1)
    processingQuip = random.choice(processingQuips)
    print(processingQuip["text"])
    progress_bar(processingQuip["timer"])

    decisionMakingQuip = random.choice(decisionMakingQuips)
    time.sleep(2)
    print(decisionMakingQuip["text"])
    time.sleep(2)
    if decisionMakingQuip["retry"]:
        continue

    print("Your decision is :", decision)
    time.sleep(2)

    action = actions.get(decision)
    if action:
        action()








