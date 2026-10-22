"""A simple command-line To-Do List application.

Tasks are stored in a JSON file beside this program, so they remain available
the next time the application is opened.
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Return saved tasks, or an empty list when no tasks have been saved."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list to disk."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def show_tasks(tasks):
    """Print all tasks and their current status."""
    if not tasks:
        print("\n--- Your To-Do List ---")
        print("No tasks have been added yet.")
        print("Choose option 2 to add your first task.")
        return

    print("\nYour To-Do List")
    print("-" * 55)
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. [{status}] {task['title']}")
        if task["description"]:
            print(f"   Description: {task['description']}")
    print("-" * 55)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("A task title cannot be empty.")
        return

    description = input("Description (optional): ").strip()
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")


def get_task_number(tasks, prompt):
    """Get a valid one-based task number from the user."""
    if not tasks:
        print("There are no tasks to select.")
        return None
    try:
        number = int(input(prompt))
        if 1 <= number <= len(tasks):
            return number - 1
    except ValueError:
        pass
    print("Please enter a valid task number.")
    return None


def update_task(tasks):
    show_tasks(tasks)
    index = get_task_number(tasks, "Task number to update: ")
    if index is None:
        return

    task = tasks[index]
    title = input(f"New title [{task['title']}]: ").strip()
    description = input("New description (leave blank to keep current): ").strip()
    if title:
        task["title"] = title
    if description:
        task["description"] = description
    save_tasks(tasks)
    print("Task updated successfully.")


def mark_complete(tasks):
    show_tasks(tasks)
    index = get_task_number(tasks, "Task number to mark as complete: ")
    if index is None:
        return

    tasks[index]["completed"] = True
    save_tasks(tasks)
    print("Task marked as complete.")


def delete_task(tasks):
    show_tasks(tasks)
    index = get_task_number(tasks, "Task number to delete: ")
    if index is None:
        return

    deleted = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted task: {deleted['title']}")


def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Mark task as complete")
    print("5. Delete task")
    print("6. Exit")


def main():
    tasks = load_tasks()
    print("Welcome to the To-Do List Application!")

    actions = {
        "1": lambda: show_tasks(tasks),
        "2": lambda: add_task(tasks),
        "3": lambda: update_task(tasks),
        "4": lambda: mark_complete(tasks),
        "5": lambda: delete_task(tasks),
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        action = actions.get(choice)
        if action:
            action()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
