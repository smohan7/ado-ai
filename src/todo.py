#!/usr/bin/env python3
"""
Simple to-do list CLI application.

This module provides a command-line interface for managing to-do tasks.
Tasks are persisted in a JSON file.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any


TASKS_FILE = Path(__file__).parent.parent / "tasks.json"


def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from the JSON file."""
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to the JSON file."""
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description: str) -> None:
    """Add a new task to the list.
    
    Args:
        description: The task description.
    """
    tasks = load_tasks()
    task_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    
    new_task = {
        "id": task_id,
        "description": description,
        "completed": False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✓ Task added: {description} (ID: {task_id})")


def list_tasks() -> None:
    """Display all tasks."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found. Add one with: python src/todo.py add <description>")
        return
    
    print("\n📋 To-Do List:")
    print("-" * 50)
    
    for task in tasks:
        status = "✓" if task.get("completed") else "○"
        task_id = task.get("id", "?")
        description = task.get("description", "")
        print(f"  {status} [{task_id}] {description}")
    
    print("-" * 50)
    completed = sum(1 for t in tasks if t.get("completed"))
    print(f"Total: {len(tasks)} | Completed: {completed}")


def main() -> None:
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="Simple to-do list manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/todo.py add "Buy groceries"
  python src/todo.py list
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    
    # List command
    subparsers.add_parser("list", help="Display all tasks")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
