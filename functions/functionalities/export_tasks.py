import random
import time
from pathlib import Path

import data
from functions.functions import progress_bar


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

def export_tasks_to_txt():
    data.tasks.sort(key=lambda task: task["priority"], reverse=True)
    with open(data.filePathTxt, "w") as file:
        for task in data.tasks:
            file.write(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}\n")