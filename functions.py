import random
import time
import data
from tqdm import tqdm



def view_tasks():
    print("Here are your tasks:")
    for task in data.tasks:
        print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}")
        time.sleep(.15)

def add_task():
    print("Adding task...")

def remove_task():
    print("Removing task...")

def exit_app():
    print("Exiting...")

def progress_bar(range_value):
    end = random.randint(5, range_value)

    for i in tqdm(range(end), desc="Processing", bar_format="{l_bar}{bar}"):
        time.sleep(1)
