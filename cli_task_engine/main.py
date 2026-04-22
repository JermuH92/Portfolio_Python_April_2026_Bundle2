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

def create_router(store):

    routes = {
        "get": store["get"],
        "add": store["add"],
        "complete": store["complete"],
        "remove": store["remove"],
    }

    def handle_command(command, argument=None):

            if command not in routes:
                return f"Unknown command '{command}'"

            if command == "get":
                return routes[command]()  

            else:
                return routes[command](argument) 
                          
    return handle_command



def run_cli(router):
    print("********* Welcome to CLI Task Engine *********")
    print("Type 'quit' to exit or type 'help' to get help on how to use the program.")
    

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye.")
            break

        if user_input.lower() == 'help':
            print("\nUsage: Add tasks to storage e.g by typing: 'add Go for a walk', \nthe program will automatically separate the command and task")
            print("as separate arguments.")
            print("To remove a task, type it's ID number, 'remove 1' ")
            print("To mark task as completed, type: 'complete 1'")
            print("To get the list of tasks saved to the list, type: 'get tasks' or 'get'\n")
            continue

        input_split = user_input.split(" ", 1)
        command = input_split[0]
        
        if len(input_split) > 1:
            arg = input_split[1]

        else:
            arg = None

        if arg is not None and (command == "complete" or command == "remove"):
            arg = int(arg)
        
        result = router(command, arg)

        if result is not None:
            print(result)



def main():

    my_store = create_store()
    app_router = create_router(my_store)
    run_cli(app_router)

if __name__ == "__main__":
    main()