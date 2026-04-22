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