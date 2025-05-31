# Simple To-Do List App
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added!")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print("Task not found!")

def view_tasks():
    if todo_list:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty!")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
