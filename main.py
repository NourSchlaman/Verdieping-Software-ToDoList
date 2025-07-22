import random
import time

tasks = [
    {"id":1 ,"name": "1000 pushups", "priority": 8},
    {"id":2 ,"name": "Heel veel aardbeien eten", "priority": 3},
    {"id":3 ,"name": "afvallen", "priority": 10},
]

decisionMakingQuips = [
    {"text": "Thank you for your Critical Decision Making", "retry": False},
    {"text": "You thought long and hard about that decision", "retry": False},
    {"text": "Are you sure about that?", "retry": False},
    {"text": "hmmmm, interesting choice", "retry": False},
    {"text": "You must have given that a lot of thought", "retry": False},
    {"text": "I wouldn't have made that choice", "retry": False},
    {"text": "NOOO PLEASE NOT THAT ONE", "retry": True},
    {"text": "Sorry for the inconvenience, but that choice is not available at the moment", "retry": True},
    {"text": "ERROR - Something went wrong", "retry": True}
]

processingQuips = [
    "Processing...",
    "Lemme think about that one...",
    "Hhmmm, this won't take long...",
    "I'm thinking, one moment please...",
    "Thinking..."
]


print("Welcome to your To-Do list Task Manager Tool")
time.sleep(1)
while True:
    print("What would you like to do?")
    time.sleep(1)
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
    print(random.choice(processingQuips))
    time.sleep(1)

    decisionMakingQuip = random.choice(decisionMakingQuips)
    time.sleep(2)
    print(decisionMakingQuip["text"])
    time.sleep(2)
    if decisionMakingQuip["retry"]:
        continue

    print("Your decision is :", decision)
    time.sleep(2)








