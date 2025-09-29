def todo_list():
    task_list = []
    
    while True:
        print("\n===Welcome to your To-Do List===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("4. Delete Task")
        
        choice = input("--Please choose an option here: ")
        
        if choice == '1':
            try:
                number_of_tasks = int(input("--How many tasks do you want to add?:")) 
            
                for i in range(number_of_tasks):
                    task = input("--Enter task: ")
                    task_list.append(task)
                print("--Task(s) added successfully.--")
            except ValueError:
                print("--Please enter a valid number.--")
            
                
        if choice == '2':
            if not task_list:
                print("--No tasks available.--")
            else:
                for task_index, task in enumerate(task_list):
                    print(f"{task_index + 1}. {task}")
        
        if choice == '3':
            print("---Exiting the To-Do list. Bye!---")
            break
        
        if choice == '4':
            if not task_list:
                print("--No tasks to delete.--")
            else:
                for task_index, task in enumerate(task_list):
                    print(f"{task_index + 1}. {task}")
                    
                try:
                    task_number = int(input("--Enter the task number to delete:"))
                    if 1 <= task_number <= len(task_list):
                        delete_task = task_list.pop(task_number - 1)
                        print(f"---Task {delete_task} deleted successfully.---")
                    else:
                        print("--Invalid task number.--")
                except ValueError:
                        print("--Enter a valid number.--")
todo_list()
                        
                    
                    
                    
        
        
            

                        