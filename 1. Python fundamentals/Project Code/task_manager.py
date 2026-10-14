#List

task_list = []

"""
1. View all Tasks
2. Add a new task
3. Add shift a new task above a specific task
4. Remove a task
5. Backup tasks
6. Swap Two Tasks
7. Clear all tasks
8. Exit
"""

# For & While

while True:
    print("\nTask Manager Menu:")
    print("1. View all Tasks")
    print("2. Add a new Task")
    print("3. Add a new task above a specific task")
    print("4. Remove a task")
    print("5. Backup tasks")
    print("6. Swap Two Task")
    print("7. Clear all tasks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("View all Tasks")
        if len(task_list) == 0:
            print("No tasks are available.")
        else:
            for task in task_list:
                print(task)
    elif choice == '2':
        new_task = input("Enter a new task:")
        task_list.append(new_task)
        print("New Task is added Successfully.")
    elif choice =='3':
        new_sp_task = input("Enter a new sp task:")
        index_of_task = int(input("Enter the index:"))

        if len(task_list) == 0 and len(task_list) < index_of_task:
            task_list.append(new_sp_task)
            print("New Task is added Successfully.")
        else:
            task_list.insert(index_of_task, new_sp_task)
            print("New Task is added Successfully.")
    elif choice == '4':
        if len(task_list) == 0:
            print("Task List is Empty.")
        else:
            task_to_remove = input("Enter the task to remove:")

            if task_to_remove in task_list:
                task_list.remove(task_to_remove)
                print("Task is removed Successfully.")
            else:
                print("Task not found in the list.")
    elif choice == '5':
        backup_task_list = task_list.copy()
        print("Backup of tasks is created successfully.")
    elif choice == '6':
        input_1st_task_index = int(input("Enter 1st task input:"))
        input_2nd_task_index = int(input("Enter 1st task input:"))
        temp_task = task_list[input_1st_task_index]
        task_list[input_1st_task_index] = task_list[input_2nd_task_index]
        task_list[input_2nd_task_index] = temp_task
    elif choice == '7':
        task_list.clear()
        print("All tasks are cleared successfully.")
    elif choice == '8':
        print("All Tasks Are done.")
        break
    else:
        print("Invalid Input")

#List
# While
#For Loop
# If - Else