todo_list = []

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task description: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully.")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

def mark_completed():
    view_tasks()
    if not todo_list:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed = todo_list.pop(task_number - 1)
            print(f"Task '{removed['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")

    input("\nPress Enter to choose another option...")
