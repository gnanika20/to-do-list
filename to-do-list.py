tasks=[]
com_tasks=[]
deleted_tasks=[]
def display_tasks(task_list,symbol=""):
    if len(task_list)==0:
        print("\n-------------------------------------\n.....No Tasks.....\n-------------------------------------\n")
    else:
        for i,task in enumerate(task_list,start=1):
            print(f"{i}.{task}{symbol}\n-------------------------------------\n")  #task in print is the actual element from task_list
def view_tasks(select,tasks,com_tasks,deleted_tasks):
    if select==1:
        if len(tasks)==0:
                print("\n-------------------------------------\n.....No Tasks.....\n-------------------------------------\n")
        else:
            print("\n-------------------------------------\nYour Current Pending Tasks are:\n")
            display_tasks(tasks,"☐")
    elif select==2:
        if len(com_tasks)==0:
                print("\n-------------------------------------\n.....No Completed Tasks.....\n-------------------------------------\n")
        else:
            print("\n-------------------------------------\nYour Completed Tasks are:\n")
            display_tasks(com_tasks,"☑")
    elif select==3:
        if len(deleted_tasks)==0:
                print("\n-------------------------------------\n.....No Deleted Tasks.....\n-------------------------------------\n")
        else:
            print("\n-------------------------------------\nYour deleted Tasks are:\n")
            display_tasks(deleted_tasks,"☒")
def task_manage(choice,tasks,com_tasks,deleted_tasks):
    try:
        if choice==1:
            print("\nAdd your task:")
            addtask=input()
            tasks.append(addtask)
            print("\nTask added successfully\n")
        elif choice==2:
            print("\n-------------------------------------\nEnter Which Tasks do you want to view\n1.To Do\n2.Completed\n3.Deleted\n")
            select=int(input())
            if select>0 and select<4:
                view_tasks(select,tasks,com_tasks,deleted_tasks)
            else:
                print("\n-------------------------------------\nEnter a valid number(1-3)\n")
        elif choice==3:
            if len(tasks)==0:
                print("\n-------------------------------------\n....No Tasks to mark finished....\nAdd tasks Now\n-------------------------------------\n")
            else:
                print("\nYour Current Tasks are:\n")
                display_tasks(tasks) 
                print("\nEnter task number you want to mark finished:\n")              
                mark_fini=int(input())
                if mark_fini>0 and mark_fini<=len(tasks):
                    com_tasks.append(tasks[mark_fini-1])
                    tasks.pop(mark_fini-1)
                else:
                    print("\nEnter a valid task number\n")
        elif choice==4:
            if len(tasks)==0:
                print("\n-------------------------------------\n....No Tasks to delete....\nAdd tasks Now\n-------------------------------------\n")
            else:
                print("\nYour Current Tasks are:\n")
                display_tasks(tasks)
                print("\nEnter the task number you want to delete:\n")
                del_task=int(input())
                if del_task>0 and del_task<=len(tasks):
                    deleted_tasks.append(tasks[del_task-1])
                    tasks.pop(del_task-1)
                    print("\nTask Deleted Successfully\n")
                else:
                    print("\nEnter a valid task number to delete\n")
        elif choice==5:
            print("\nExiting....")
        else:
            print("\nEnter a valid choice\n")
    except ValueError:
        print("\nEnter a valid integer\n")
while True:
    print("\n-------------------------------------\n")
    print("\n1.Add Task")
    print("\n2.View Task")
    print("\n3.Mark Finished")
    print("\n4.Delete Task")
    print("\n5.Exit\n")
    try:
        choice=int(input("Enter your choice:"))
        print("\n-------------------------------------\n")
        task_manage(choice,tasks,com_tasks,deleted_tasks)
        if choice==5:
            break
    except ValueError:
        print("\nEnter valid integer as choice\n") #python To-do-list.py
