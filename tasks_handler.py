import sys
import json_handlers

VALID_STATUSES = ("todo", "in-progress", "done")

def add_task(description):
    tasks = json_handlers.load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": json_handlers.now(),
        "updatedAt": json_handlers.now()
    }
    tasks.append(task)
    json_handlers.save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def find_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None

def parse_id(value):
    try:
        return int(value)
    except ValueError:
        print(f"Invalid ID: '{value}' (must be a number)")
        sys.exit(1)

def update_task(task_id, description):
    tasks = json_handlers.load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"No task with ID {task_id}")
        return
    
    task["description"] = description
    task["updatedAt"] = json_handlers.now()
    json_handlers.save_tasks(tasks)
    print("Task updated successfully")

def delete_task(task_id):
    tasks = json_handlers.load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"No task with ID {task_id}")
        return
    tasks.remove(task)
    json_handlers.save_tasks(task)
    print("deleted")

def set_status(task_id, status):
    tasks = json_handlers.load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"No task with ID {task_id}")
        return
    task["status"] = status
    task["updatedAt"] = json_handlers.now()
    json_handlers.save_tasks(tasks)
    print(f"Task {task_id} marked as {status}")

def list_tasks(status=None):
    if status and status not in VALID_STATUSES:
        print(f"Invalid status '{status}'. Use {', '.join(VALID_STATUSES)}")
        return
    tasks = json_handlers.load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if not tasks:
        print("No tasks found.")
    for t in tasks:
        print(f"[{t['id']}] {t['description']} ({t['status']}) - updated {t['updatedAt']}")