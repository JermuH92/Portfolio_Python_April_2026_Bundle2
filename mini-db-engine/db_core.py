import json
from router import create_router
from cli import run_cli

def create_database(filename="database.json"):
    tables = {}
    counters = {}

    try:
        with open(filename, "r") as file:
            db_state = json.load(file)
            tables = db_state["tables"]
            counters = db_state["counters"]

    except FileNotFoundError:
        pass


    def _save_state():
        db_state = {"tables": tables, "counters": counters}

        with open(filename, "w") as file:
            json.dump(db_state, file)


    def create_table(table_name):
        tables[table_name] = []
        counters[table_name] = 1
        _save_state()


    def insert(table_name, record):

        if table_name not in tables:
            return f"Error: Table '{table_name}' does not exist."
        
        fetch_id = counters[table_name]
        record["id"] = fetch_id
        counters[table_name] += 1

        tables[table_name].append(record)
        _save_state()
        return f"Record inserted into{table_name}"


    def find_by_id(table_name, record_id):

        if table_name not in tables:
            return f"Error: Table '{table_name} does not exist."
        
        for record in tables[table_name]:
            if record["id"] == record_id:
                return record
            
        return None


    def find_by(table_name, condition_func):
        
        if table_name not in tables:
            return f"Error: Table '{table_name} does not exist."
        
        results = []

        for record in tables[table_name]:
            if condition_func(record):
                results.append(record)

        return results


    def update_by_id(table_name, record_id, updates):

        if table_name not in tables:
            return f"Error: Table '{table_name} does not exist."
        
        record_to_update = find_by_id(table_name, record_id)

        if record_to_update is None:
            return f"Error: {table_name} with {record_id} does not exist"

        record_to_update.update(updates)
        _save_state()
        return f"Record {record_id} UPDATED successfully."


    def delete_by_id(table_name, record_id):

        if table_name not in tables:
            return f"Error: Table '{table_name} does not exist."
        
        record_to_delete = find_by_id(table_name, record_id)

        if record_to_delete is None:
            return f"Error: {table_name} with {record_id} does not exist"
        
        tables[table_name].remove(record_to_delete)
        _save_state()
        return f"Record {record_id} DELETED successfully."
        
        


    return {
        "create_table": create_table,
        "insert": insert,
        "get_all": lambda: tables,
        "find_by_id": find_by_id,
        "find_by": find_by,
        "update_by_id": update_by_id,
        "delete_by_id": delete_by_id
    }


def main():

    my_db = create_database()

    app_router = create_router(my_db)

    run_cli(app_router)

if __name__ == "__main__":
    main()

