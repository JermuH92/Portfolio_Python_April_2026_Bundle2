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
    return {
        "get": get_tasks,
        "add": add_task
    }
    
    

my_store = create_store()
my_store["add"]("Buy soda")
my_store["add"]("Code a database")

print(my_store["get"]())