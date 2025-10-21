
FILENAME = "tasks.txt"


def load_tasks():
 
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" | ")
                    if len(parts) == 2:
                        tasks.append({"task": parts[0], "done": parts[1] == "True"})
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']} | {t['done']}\n")


def show_tasks(tasks):
    
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n==== YOUR TODO LIST ====")
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()


def add_task(tasks):

    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!\n")
    else:
        print("Empty task cannot be added!\n")


def remove_task(tasks):

    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['task']}' removed successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def mark_complete(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter the task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num - 1]['task']}' marked as complete!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    
    tasks = load_tasks()

    while True:
        print("========= TODO LIST MENU =========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task Complete")
        print("5. Exit")
        print("==================================")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("Goodbye! Tasks saved permanently.")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
