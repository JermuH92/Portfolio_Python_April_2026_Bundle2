def run_cli(router):
    print("********* Welcome to Multi-Table DB Engine *********")
    print("Commands (e.g): create_table users | insert users {\"name\": \"Jere\"} | get_all | quit")
    print("Type 'help' to get a list of usable commands")

    while True:
        user_input = input("> ").strip()
        if not user_input: continue
        
        if user_input.lower() == "quit": break

        if user_input.lower() == "help":
            print("List of commands....") # update later
            continue

        parts = user_input.split(" ", 2)

        command = parts[0]
        table_name = parts[1] if len(parts) > 1 else None
        data_str = parts[2] if len(parts) > 2 else None

        result = router(command, table_name, data_str)
        if result is not None:
            print(result)