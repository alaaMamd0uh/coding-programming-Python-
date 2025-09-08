import json

def load_data():
    try:
        with open("dados.json", "r") as f: # read the file law mawgood
            return json.load(f)
    except FileNotFoundError: # if its not make list fadya
        return []

def save_data(data):
    with open("dados.json", "w") as f: # law 3awz a3ml save l new data fe json file
        json.dump(data, f)

class Task:
    def __init__(self, task, deadline, task_type):
        self.task = task
        self.deadline = deadline
        self.task_type = task_type
        self.status = "incomplete" # start incompleter

    def to_dict(self): #convert task into dictionary
        return {
            "task": self.task,
            "deadline": self.deadline,
            "type": self.task_type,
            "status": self.status
        }

class PersonalTask(Task):
    def __init__(self, task, deadline, category):
        super().__init__(task, deadline, "personal") # call the init of task and make it personal
        self.category = category

    def to_dict(self):
        data = super().to_dict()
        data["category"] = self.category  # 5adna el list mn el task w added category
        return data

class WorkTask(Task): # the same as personal class but for the work
    def __init__(self, task, deadline, priority):
        super().__init__(task, deadline, "work")
        self.priority = priority # new feature -> priority = high aw low aw medium

    def to_dict(self):
        data = super().to_dict() # call el class to dictionary
        data["priority"] = self.priority # w n3ml add lel new priority
        return data
class ManagementTask:
    def __init__(self):
        self.data = load_data() # da ely bymanage kol el opeerations - > add , delete , show ...

    def create(self):
        kind = input("enter task type personal or work ").strip().lower()  # lower 3a4an ma5leha ta7t fel condition lower case
        task = input("enter task title ")
        deadline = input("enter deadline")

        if kind == "personal":
            category = input("enter category:")
            newtask = PersonalTask(task, deadline, category)
        elif kind == "work":
            priority = input("enter priority ")
            newtask = WorkTask(task, deadline, priority)

        else:
            print("invalid")
            return

        self.data.append(newtask.to_dict())
        save_data(self.data)
        print("task added successfully")



def delete_Task(): #function to delete task from  allTask >> list of dict ــ using index

    allTasks = load_data() # load all tasks
    if not allTasks: # check if list is empty
        print("No tasks found to delete")
    else:
        count = 1  # start counter for numbering

        for task in allTasks:
            print(f"{count}. {task['task']} ,{task['type']}, {task['deadline']}")
            count += 1 #increase counter
        deleIndex = int(input("Enter the number of the task you want to delete: "))#user chooses task
        allTasks.pop(deleIndex - 1) #remove chosen task
        save_data(allTasks)# save update
        print("Task deleted successfully")

def Update_deadline():#function to update the deadline from  allTask >> list of dict ــ using index
    allTasks = load_data()
    if not allTasks:
        print("No tasks found to Update")
    else:
        count = 1
        for task in allTasks:
            print(f"{count}.{task['task']} , {task['deadline']}\n")
            count += 1
        updateIndex = int(input("Enter the number of the task you want to update: "))#user chooses task bl index
        new_deadline = input("Enter the new deadline: ") # user enters the new deadline he wants to save the task
        allTasks[updateIndex - 1]["deadline"] = new_deadline #update the deadline of the selected task
        save_data(allTasks)
        print("Task updated successfully")

def mark_for_complete():
    allTasks = load_data()# load all tasks
    if not allTasks:
        print("No tasks found to Mark as Completed")
    else:
        for i, task in enumerate(allTasks):
            # enumerate >> == count
            # loop 3la el list w akhod el index (i) + el task nafsaha
            # i+1 hwa el counter zay lama astakhdem count variable
            print(f"{i + 1}. task: {task['task']} , (status: {task['status']}) ")
        compIndex = int(input("Enter the number of the task you want to mark as completed: "))#user chooses task bl index
        allTasks[compIndex - 1]["status"] = "completed"
        save_data(allTasks)
        print("Task completed successfully")


#Main Menu
print("Welcome to SIC Task Manager")
while True:
    print("")
    print("Please choose an option:\n "
          "[1] Add a Task\n "
          "[2] View All Tasks\n "
          "[3] Delete a Task\n "
          "[4] Update a Deadline\n "
          "[5] Mark Task as Completed\n "
          "[0] Exit\n")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("value error")
        print("try again")
        choice = int(input("Enter your choice: "))

    finally:
        print("thanck you")

    if choice == 1:
            newTask = ManagementTask()  # Create a new ManagementTask object
            newTask.create()  # call create() >> to add a new task

    elif choice == 2:
            allTasks = load_data()  # load all tasks from JSON
            for task in allTasks:  # loop through tasks
                print(task)

    elif choice == 3:
            delete_Task()  # call function to delete a task

    elif choice == 4:
            Update_deadline()  # call function to update a deadline

    elif choice == 5:
            mark_for_complete()  # call function to mark task as completed

    elif choice == 0:
            confirm_exit = input("Are you sure you want to exit ? (yes/no) ").lower()
            if confirm_exit == "yes":
                print("Bye, bye")
                print("Thank you for using SIC Task Manager")
                break

    else:
            print("invalid choice")
