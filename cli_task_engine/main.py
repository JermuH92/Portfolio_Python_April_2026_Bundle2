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
    print("***** Welcome to CLI Task Engine *****\n")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye.")
            break

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