import json

def create_store(filename="tasks.json"):
    tasks = []
    next_id = 1

    try:
        with open(filename, "r") as file:
            tasks = json.load(file)

            if len(tasks) > 0:
                next_id = tasks[-1]["id"] + 1
    
    except FileNotFoundError:
        pass
    
    def _save_state():
        with open(filename, "w") as file:
            json.dump(tasks, file)


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

        _save_state()
        return f"---TASK ADDED: '{task_name}' (ID: {new_task_dict['id']})"


    def complete_task(task_id):

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
        
        _save_state()
        return f"---TASK COMPLETED (ID:'{task_id}')"

    def remove_task(task_id):

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                break
        
        _save_state()
        return f"---TASK REMOVED (ID:'{task_id}')"

    return {

        "get": get_tasks,
        "add": add_task,        
        "complete": complete_task,
        "remove": remove_task

    }