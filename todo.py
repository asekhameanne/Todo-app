class TodoApp:

    def __init__(self):
        self.database = []

    def add_task(self):
        task = input("Enter task: ").strip()

        if not task:
            print("Task cannot be empty")
            return

        self.database.append(task)
        print("Task added")

    def view_task(self):
        if not self.database:
            print("No tasks")
        else:
            for no, task in enumerate(self.database, 1):
                print(f"{no}. {task}")

    def delete_task(self):
        if not self.database:
            print("No tasks")
            return

        self.view_task()

        try:
            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(self.database):
                deleted_task = self.database.pop(task_number - 1)
                print(f"{deleted_task} deleted successfully")
            else:
                print("invalid task number")
        except ValueError:
            print("input valid number")

    def run(self):
        print("ANNE'S Todo app")
        while True:
            print("""
1. Add Task
2. View Task
3. Delete Task
4. Exit
            """)

            choice = input("input choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("see you next time")
                break
            else:
                print("invalid option")


app = TodoApp()
app.run()