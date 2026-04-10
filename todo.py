import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return file.read().splitlines()
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

# Main program
tasks = load_tasks()

while True:
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")

    elif choice == '2':
        show_tasks(tasks)

    elif choice == '3':
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to update: "))
            if 0 < num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[num-1] = new_task
                save_tasks(tasks)
                print("✏️ Task updated successfully!\n")
            else:
                print("❌ Invalid task number!\n")
        except:
            print("❌ Please enter a valid number!\n")

    elif choice == '4':
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
                print("🗑️ Task deleted successfully!\n")
            else:
                print("❌ Invalid task number!\n")
        except:
            print("❌ Please enter a valid number!\n")

    elif choice == '5':
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice! Try again.\n")