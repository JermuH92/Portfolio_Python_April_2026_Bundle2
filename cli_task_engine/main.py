def create_store():
    tasks = []

    def get_tasks():
        return tasks
    
    def add_task(task_name):
        new_id = len(tasks) + 1
        
        new_task_dict = {
            "id": new_id,
            "name": task_name,
            "completed": False
        }
        tasks.append(new_task_dict)


    def complete_task(task_id):
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True


    return {

        "get": get_tasks,
        "add": add_task,
        "complete": complete_task

    }


    

my_store = create_store()
my_store["add"]("Buy soda")
my_store["add"]("Code a database")
my_store["add"]("Practice closures")

my_store["complete"](1)
my_store["complete"](2)

print(my_store["get"]())