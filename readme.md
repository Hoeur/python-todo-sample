# To-Do List Application

## Description
This is a simple command-line To-Do List application written in Python. It allows users to add, view, mark tasks as completed, delete tasks, and save/load tasks using a JSON file.

## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Save and load tasks from a JSON file

## Requirements
- Python 3.x

## Setup Instructions

1. **Clone the repository**
```sh
  git clone https://github.com/Hoeur/python-todo-sample.git
  cd todo-list
```

2. **Run the application**
```sh
  python todo.py
```

## Usage

1. Run the script by executing `python todo.py`.
2. Follow the on-screen menu:
   - Press `1` to add a task.
   - Press `2` to view all tasks.
   - Press `3` to mark a task as completed.
   - Press `4` to delete a task.
   - Press `5` to exit the application.

## File Structure
```
.
├── tasks.json        # Stores task data
├── todo.py           # Main script
├── README.md         # Setup and usage instructions
```

## Saving and Loading Tasks
- Tasks are saved in `tasks.json`.
- The application automatically loads saved tasks when started.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

