from store import create_store
from router import create_router
from cli import run_cli


def main():
    # Creates a database (from store.py)
    my_store = create_store()

    # Creates an app router and hands DB over to the router (from router.py)
    app_router = create_router(my_store)

    # Runs user-interface and hand it the router (from cli.py)
    run_cli(app_router)

if __name__ == "__main__":
    main()