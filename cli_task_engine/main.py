def create_store():
    tasks = []
    next_id = 1

    def get_tasks():
        return tasks
    
    def add_task(task_name):
        nonlocal next_id
        
        new_task_dict = {
            "id": next_id,
            "name": task_name,
            "completed": False
        }
        tasks.append(new_task_dict)
        next_id = next_id + 1


    def complete_task(task_id):

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True

    def remove_task(task_id):

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                break

    return {

        "get": get_tasks,
        "add": add_task,        
        "complete": complete_task,
        "remove": remove_task

    }


    

my_store = create_store()
my_store["add"]("Buy soda")
my_store["add"]("Code a database")
my_store["add"]("Practice closures")

my_store["complete"](1)
my_store["complete"](2)
my_store["remove"](2)
my_store["add"]("BugTest")
my_store["remove"](1)
my_store["add"]("CheckIDIncrement")

print(my_store["get"]())