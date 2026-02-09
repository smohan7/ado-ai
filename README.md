# ADO-AI: Simple To-Do List CLI

A lightweight, command-line to-do list manager built with Python. This project demonstrates a simple CLI application using `argparse` for command parsing and JSON for persistent task storage.

## Features

- **Add Tasks**: Create new to-do items with natural descriptions
- **List Tasks**: View all tasks with their completion status
- **Task Tracking**: Tasks are persisted in JSON format for reliable storage
- **Simple Interface**: Easy-to-use command-line commands

## Project Structure

```
ado-ai/
├── src/
│   └── todo.py          # Main CLI application
├── tasks.json           # Task storage (auto-generated)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/smohan7/ado-ai.git
   cd ado-ai
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

### Add a Task

```bash
python src/todo.py add "Buy groceries"
python src/todo.py add "Complete project documentation"
```

### List All Tasks

```bash
python src/todo.py list
```

### View Help

```bash
python src/todo.py --help
```

## Example Output

```
📋 To-Do List:
--------------------------------------------------
  ○ [1] Buy groceries
  ✓ [2] Complete project documentation
--------------------------------------------------
Total: 2 | Completed: 1
```

## Task Storage

Tasks are automatically saved to `tasks.json` in JSON format:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "description": "Complete project documentation",
    "completed": true
  }
]
```

## Development

This is a simple skeleton for a to-do list CLI application. Future enhancements could include:
- Mark tasks as complete
- Delete tasks
- Edit task descriptions
- Filter by completion status
- Due dates and priorities
- Export/import tasks

## License

This project is open source and available under the MIT License.