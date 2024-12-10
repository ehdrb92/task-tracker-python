import sys


from app_service import AppService


def main(args: list):
    # init application
    app_service = AppService()
    app_service.init_tasks()

    # Route Service
    if args[0] == "add":
        return

    if args[0] == "update":
        return

    if args[0] == "delete":
        return

    if args[0] == "list":
        return

    if args[0].startswith("mark"):
        return

    return


if __name__ == "__main__":
    main(sys.argv[1:])
