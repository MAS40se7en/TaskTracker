# Task Tracker CLI

A simple command line app to track what you need to do, what you're working on, and what you've finished. Tasks are stored in a local `tasks.json` file.

## Requirements

- Python 3 (no external libraries needed)

## Usage

Run commands from the project folder:

```bash
python task_tracker.py <command> [arguments]
```

On Windows you can also use `py task_tracker.py ...`.

### Commands

| Command | Description |
|---|---|
| `add "description"` | Add a new task |
| `update <id> "new description"` | Change a task's description |
| `delete <id>` | Delete a task |
| `mark-in-progress <id>` | Mark a task as in progress |
| `mark-done <id>` | Mark a task as done |
| `list` | List all tasks |
| `list todo` | List tasks not started |
| `list in-progress` | List tasks in progress |
| `list done` | List completed tasks |

### Examples

```bash
python task_tracker.py add "Buy groceries"
# Task added successfully (ID: 1)

python task_tracker.py update 1 "Buy groceries and cook dinner"
python task_tracker.py mark-in-progress 1
python task_tracker.py list in-progress
python task_tracker.py mark-done 1
python task_tracker.py delete 1
```

## Task properties

Each task in `tasks.json` has:

- `id`: unique number
- `description`: what needs to be done
- `status`: `todo`, `in-progress`, or `done`
- `createdAt`: when it was created
- `updatedAt`: when it was last changed

## Notes

- `tasks.json` is created automatically in the folder you run the command from.
- Wrap descriptions containing spaces in quotes.

## Roadmap PROJECT URL
https://roadmap.sh/projects/task-tracker
