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
        
        elif command == "find":
            if not table_name or not data_str:
                return "Error: Give a table and ID (e.g. find users 1)"
            try:
                record_id = int(data_str)
                result = db["find_by_id"](table_name, record_id)
                return result if result is not None else f"Record {record_id} not found."
            except ValueError:
                return "Error: ID must be a number."

        elif command == "delete":
            if not table_name or not data_str:
                return "Error: Give a table and ID (e.g. delete users 1)"
            try:
                record_id = int(data_str)
                return db["delete_by_id"](table_name, record_id)
            except ValueError:
                return "Error: ID must be a number."
        
        elif command =="update":
            if not table_name or not data_str:
                return "Error: Give table, ID and JSON (e.g. update users 1 {\"age\": 35})"
            try:
                id_str, json_str = data_str.split(" ", 1)
                record_id = int(id_str)
                updates = json.loads(json_str)

                return db["update_by_id"](table_name, record_id, updates)
            except ValueError:
                return "Error: ID must be a number."
            except json.JSONDecodeError:
                return "Error: Data is not valid JSON format."

        else:
            return f"Unknown Command: {command}"
    
    return handle_command
 