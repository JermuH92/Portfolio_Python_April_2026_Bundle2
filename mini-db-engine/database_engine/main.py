from router import create_router
from cli import run_cli
from db_core import create_database

def main():

    my_db = create_database()

    app_router = create_router(my_db)

    run_cli(app_router)

if __name__ == "__main__":
    main()