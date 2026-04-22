def create_database():
    tables = {}

    def create_table(table_name):
        tables[table_name] = []
        
    
    def insert(table_name, record):

        if table_name not in tables:
            return f"Error: Table '{table_name}' does not exist."

        tables[table_name].append(record)

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



    return {
        "create_table": create_table,
        "insert": insert,
        "get_all": lambda: tables,
        "find_by_id": find_by_id,
        "find_by": find_by
    }



my_db = create_database()
my_db["create_table"]("users")
my_db["create_table"]("products")

my_db["insert"]("users", {"id": 1, "name": "John", "age": 49})
my_db["insert"]("products", {"id": 101, "name": "Coffee"})
my_db["insert"]("users", {"id": 2, "name": "Hans", "age": 52})
my_db["insert"]("users", {"id": 3, "name": "Holly", "age": 48})
my_db["insert"]("users", {"id": 4, "name": "Lucy", "age": 6})

result = my_db["find_by_id"]("users", 1)
print("Found user", result)

adult_users = my_db["find_by"]("users", lambda user: user.get("age", 0) >= 18)
print("Adult users:", adult_users)

print(my_db["get_all"]())
