# todo.py
"""
To-Do List Application (Command Line)
Author: Christian Stephenson
"""

tasks = []  # Store tasks in a Python list

def show_menu():
    """Display the main menu"""
    print("\n===== TO-DO LIST APP =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Quit")

def view_tasks():
    """Display tasks with validation"""
    if not tasks:
        print("⚠ No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task '{task}' added.")
    else:
        print("⚠ Task cannot be empty.")

def delete_task():
    """Delete a task by number with error handling"""
    if not tasks:
        print("⚠ No tasks to delete.")
        return
    view_tasks()
    try:
        choice = int(input("Enter the number of the task to delete: "))
        removed = tasks.pop(choice - 1)
        print(f"🗑 Task '{removed}' deleted.")
    except ValueError:
        print("⚠ Please enter a valid number.")
    except IndexError:
        print("⚠ That task number does not exist.")
    finally:
        print("Returning to menu...")

def main():
    """Main program loop"""
    print("🎉 Welcome to the To-Do List Application 🎉")
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        try:
            if choice == "1":
                view_tasks()
            elif choice == "2":
                add_task()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("⚠ Invalid option. Please choose 1–4.")
        except Exception as e:
            print(f"⚠ An unexpected error occurred: {e}")
        else:
            print("Operation completed successfully.")
        finally:
            print("---")

if __name__ == "__main__":
    main()