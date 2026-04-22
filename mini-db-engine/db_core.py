def create_database():
    tables = {}

    def create_table(table_name):
        tables[table_name] = []
        
    
    def insert(table_name, record):

        if table_name not in tables:
            return f"Error: Table '{table_name}' does not exist."

        tables[table_name].append(record)

        return f"Record inserted into{table_name}"
    
    return {
        "create_table": create_table,
        "insert": insert,
        "get_all": lambda: tables
    }

my_db = create_database()
my_db["create_table"]("users")
my_db["create_table"]("products")

my_db["insert"]("users", {"id": 1, "name": "John"})
my_db["insert"]("products", {"id": 101, "name": "Coffee"})

print(my_db["get_all"]())
