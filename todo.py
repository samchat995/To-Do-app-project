
import json
import os

# Load tasks from file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        show_tasks(tasks)
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added!")

        elif choice == "2":
            if tasks:
                try:
                    num = int(input("Enter task number to remove: "))
                    if 0 < num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Removed: {removed}")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
            else:
                print("❌ No tasks to remove.")

        elif choice == "3":
            print("👋 Goodbye! Your tasks are saved.")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
print("welcome")