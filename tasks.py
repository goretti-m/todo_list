# tasks = []

# def add_task():
#     task = input("Enter a task: ")
#     tasks.append(task)
#     print("Task added successfully!")

# def view_tasks():
#     if tasks:
#         print("Your tasks:")
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")
#     else:
#         print("No tasks found.")

# def delete_task():
#     view_tasks()
#     if tasks:
#         task_num = int(input("Enter the task number to delete: "))
#         if 1 <= task_num <= len(tasks):
#             deleted_task = tasks.pop(task_num - 1)
#             print(f"Task '{deleted_task}' deleted successfully!")
#         else:
#             print("Invalid task number.")
#     else:
#         print("No tasks found.")

# def main():
#     while True:
#         print("\n---- To-Do List ----")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Delete Task")
#         print("4. Quit")

#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             add_task()
#         elif choice == "2":
#             view_tasks()
#         elif choice == "3":
#             delete_task()
#         elif choice == "4":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
