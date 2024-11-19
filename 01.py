import json


def get_data():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or invalid JSON")
        return []


def save_tasks(data):
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


def add_task(data):
    while True:
        task_id = input("Enter task ID: ")
        if not any(task["number"] == task_id for task in data):
            break
        print("Task ID already exists.")
    task_name = input("Enter task name: ")
    data.append({"task": task_name, "number": task_id, "status": "incomplete"})
    data.sort(key=lambda x: x['number'])
    save_tasks(data)
    print("Task added.")


def view_tasks(data, status=None):
    for task in data:
        if status is None or task['status'] == status:
            print(f"ID: {task['number']}, Task: {
                  task['task']}, Status: {task['status']}")


def change_status(data):
    task_id = input("Enter task ID to mark as complete: ")
    for task in data:
        if task['number'] == task_id:
            task['status'] = "complete"
            save_tasks(data)
            print("Task marked as complete.")
            return
    print("Task not found.")


def get_input(data):
    while True:
        print("\nOptions:\n1. View all tasks\n2. View completed tasks\n3. View incomplete tasks\n4. Mark task as complete\n5. Add a task\n6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(data)
        elif choice == "2":
            view_tasks(data, status="complete")
        elif choice == "3":
            view_tasks(data, status="incomplete")
        elif choice == "4":
            change_status(data)
        elif choice == "5":
            add_task(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    data = get_data()
    get_input(data)


if __name__ == "__main__":
    main()
