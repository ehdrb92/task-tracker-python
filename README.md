# Task Tracker (Python)

Task Tracker is a task management application. You can create, view, edit, and delete tasks. You can also check only the tasks with the status you want to check.

## Usage

`git clone https://github.com/ehdrb92/task-tracker-python.git`

`cd task-tracker-python/src`

- add task: `python app.py add {description}`
- get tasks: `python app.py list {status}`
- update task description: `python app.py update {id} {description}`
- update task status: `python app.py mark-{status} {id}`
- delete task: `python app.py delete {id}`