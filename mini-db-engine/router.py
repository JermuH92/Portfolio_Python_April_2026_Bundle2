import json

def create_router(db):

    def handle_command(command, table_name=None, data_str=None):
        if command == "get_all":
            return db["get_all"]()
        
        elif command == "create_table":
            if not table_name:
                return "Error: Give a name of a table"
            
            db["create_table"](table_name)
            return f"Created table: {table_name}"

        elif command == 'insert':
            if not table_name or not data_str:
                return "Error: Give a table and JSON-data"
            try:
                record_dict = json.loads(data_str)
                db["insert"](table_name, record_dict)
                return f"Record inserted into {table_name}"
            
            except json.JSONDecodeError:
                return "Error: Data is not valid JSON format... use double quotes (e.g. {\"key\": \"value\"}))"
            
        else:
            return f"Unknown Command: {command}"
    
    return handle_command
 