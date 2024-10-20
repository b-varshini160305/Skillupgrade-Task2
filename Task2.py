class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks[task_name] = False
        print(f"Task '{task_name}' added!")

    def view_tasks(self):
        print("\nCurrent To-Do List:")
        for task, status in self.tasks.items():
            status_str = "Completed" if status else "Pending"
            print(f"{task}: {status_str}")

    def mark_completed(self):
        task_name = input("Enter task name to mark completed: ")
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked completed!")
        else:
            print(f"Task '{task_name}' not found!")

    def delete_task(self):
        task_name = input("Enter task name to delete: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted!")
        else:
            print(f"Task '{task_name}' not found!")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.mark_completed()
        elif choice == '4':
            todo.delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
