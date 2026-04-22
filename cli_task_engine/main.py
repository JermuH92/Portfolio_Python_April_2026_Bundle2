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
            print(f"Unknown command {command}")

        if command == "get":
            return routes[command]()  

        else:
            return routes[command](argument) 
                

          
    return handle_command

def main():
    my_store = create_store()

    app_router = create_router(my_store)

    app_router("add", "Buy soda")
    app_router("add", "Build an app router")
    app_router("add", "Test the router")
    app_router("remove", 2)
    app_router("complete", 1)
    app_router("add", "Test for increments")



    print(app_router("get"))

if __name__ == "__main__":
    main()