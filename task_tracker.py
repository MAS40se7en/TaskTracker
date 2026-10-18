import sys
import tasks_handler

def main():
    args = sys.argv[1:]
    if not args:
        print_usage()
        return

    command, rest = args[0], args[1:]

    if command == "add" and len(rest) == 1:
        tasks_handler.add_task(rest[0])
    elif command == "update" and len(rest) == 2:
        tasks_handler.update_task(tasks_handler.parse_id(rest[0]), rest[1])
    elif command == "delete" and len(rest) == 1:
        tasks_handler.delete_task(tasks_handler.parse_id(rest[0]))
    elif command == "list" and len(rest) <= 1:
        tasks_handler.list_tasks(rest[0] if rest else None)
    elif command == "mark-in-progress" or command == "mark-done" and len(rest) == 1:
        if command == "mark-in-progress":
            tasks_handler.set_status(tasks_handler.parse_id(rest[0]), "in progress")
        if command == "mark-done":
            tasks_handler.set_status(tasks_handler.parse_id(rest[0]), "done")
    else:
        print(f"Uknown command: {command}")
        print_usage()

def print_usage():
    print("Usage:")
    print('     task_tracker.py add "description"')
    print('     task_tracker.py update <id> "new description"')
    print('     task_tracker.py delete <id>')
    print('     task_tracker.py mark-in-progress <id>')
    print('     task_tracker.py mark-down <id>')
    print('     task_tracker.py list [todo|in-progress|done]')

if __name__ == "__main__":
    main()