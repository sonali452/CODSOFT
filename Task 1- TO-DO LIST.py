import os
import datetime

TODO_FILE = "todo.txt"


def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty.")


def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Complete Task\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            show_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("Thank you for using the To-Do List application!")


if __name__ == "__main__":
    main()
    