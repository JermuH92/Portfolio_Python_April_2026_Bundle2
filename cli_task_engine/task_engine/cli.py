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
            try:
              arg = int(arg)
            except ValueError:
                print("Error: ID must be a number.")
                continue
            
        result = router(command, arg)

        if result is not None:
            print(result)