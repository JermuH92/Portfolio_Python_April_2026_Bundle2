def run_cli(router):
    print("********* Welcome to Multi-Table DB Engine *********")
    print("Commands (e.g): create_table users | insert users {\"name\": \"Jere\"} | get_all | quit")
    print("Type 'help' to get a list of usable commands")

    while True:
        user_input = input("> ").strip()
        if not user_input: continue
        
        if user_input.lower() == "quit":
            print("Until next time...")
            break

        if user_input.lower() == "help":
            print("List of command examples....") 
            print("----------------")
            print("Create table: <create_table 'table_name'>")
            print("Insert key-value pairs into a table: <insert 'table_name' {'key_name': 'value'}>")
            print("Find: <find 'table_name'> 'ID'")
            print("Delete: <delete 'table_name' 'ID'")
            print("Update: <update 'table_name' 'ID' {'key_name': 'new_value'}>")
            continue

        parts = user_input.split(" ", 2)

        command = parts[0]
        table_name = parts[1] if len(parts) > 1 else None
        data_str = parts[2] if len(parts) > 2 else None

        result = router(command, table_name, data_str)
        if result is not None:
            print(result)