import json
import os

# The file where the to-do list is stored
TODO_FILE = "todo_list.json"

def clear_todo_list_file():
    """Delete the to-do list file to start fresh."""
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)
        print("Previous to-do list cleared. Starting with a fresh list.")

def load_todo_list():
    """Load the to-do list from the file if it exists, otherwise return an empty list."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todo_list(todo_list):
    """Save the current to-do list to the file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todo_list, f, indent=4)

def add_task(todo_list):
    """Add a new task to the to-do list."""
    task = input("What task would you like to add? ")
    todo_list.append({"task": task, "done": False})
    print(f"Task '{task}' has been added to your list.")
    save_todo_list(todo_list)

def list_tasks(todo_list):
    """Display all tasks in the to-do list with their status."""
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Here are your current tasks:")
        for i, task in enumerate(todo_list, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def delete_task(todo_list):
    """Remove a task from the to-do list based on its number."""
    try:
        task_num = int(input("Enter the number of the task you want to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"Task '{removed_task['task']}' has been removed from your list.")
            save_todo_list(todo_list)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_done(todo_list):
    """Mark a task as completed based on its number."""
    try:
        task_num = int(input("Enter the number of the task you completed: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print(f"Task '{todo_list[task_num]['task']}' has been marked as done.")
            save_todo_list(todo_list)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    clear_todo_list_file()  # Clear the to-do list file at the start
    todo_list = load_todo_list()  # Load existing tasks if there are any
    print("Welcome to your personal to-do list manager!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Mark a task as done")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            delete_task(todo_list)
        elif choice == "3":
            list_tasks(todo_list)
        elif choice == "4":
            mark_task_done(todo_list)
        elif choice == "5":
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()

