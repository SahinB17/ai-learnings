def to_do():

    print("Wellcome to your to-do program!")
    print("1.Add task\n2.View tasks\n3.Complete task\n4.Delete task\n5.Exit")

    tasks = []

    while True :
        choice = int(input("Enter your choice :"))
        if choice == 1:
            task=input("Enter task description :")
            tasks.append({"Description": task ,"Completed" : False})
            print("Task added!")

        elif choice == 2:
            for idx,task in enumerate(tasks,start =1) :
                status="Done" if task["Completed"] else "Not Done"
                print(f"{idx}.{task['Description']} -{status}")

        elif choice == 3:
            tsk =input("Enter the name of task to complete :")
            for task in tasks:
                if task['Description']==tsk:
                    task['Completed']=True
                    print("Task completed!")

        elif choice == 4 :
            delete = input("Enter the name of thetask to delete :")
            for task in tasks :
                if task['Description']==delete:
                    tasks.remove(task)
                    print("Task deleted!")

        elif choice == 5:
            print("Bye-Bye!!!")
            break
        else :
            print("Enter valid choice!")

to_do()