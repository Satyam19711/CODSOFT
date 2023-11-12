import os

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def view_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nCurrent To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("\nTo-Do List is empty.")
    else:
        print("\nTo-Do List does not exist. Create a new one.")

def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the To-Do List.")

def update_task(index, new_task):
    tasks = get_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        save_tasks(tasks)
        print(f"Task {index} updated.")
    else:
        print("Invalid task index.")

def remove_task(index):
    tasks = get_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task.strip()}' removed from the To-Do List.")
    else:
        print("Invalid task index.")

def get_tasks():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open("todo.txt", "w") as file:
        file.writelines(tasks)

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_todo_list()

    elif choice == '2':
        task = input("Enter the new task: ")
        add_task(task)

    elif choice == '3':
        view_todo_list()
        index = int(input("Enter the index of the task to update: "))
        new_task = input("Enter the updated task: ")
        update_task(index, new_task)

    elif choice == '4':
        view_todo_list()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)

    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


#THANKYOU