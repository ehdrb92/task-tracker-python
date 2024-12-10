import sys
from datetime import datetime


from app_service import AppService
from task import Task


def main(args: list) -> None:
    try:
        # init application
        app_service = AppService()
        app_service.init_tasks()

        # Route Service
        if args[0] == "add":
            task = Task(
                id=app_service.last_id,
                decription=args[1],
                status="todo",
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            app_service.create_task(task)

        if args[0] == "update":
            pass

        if args[0] == "delete":
            pass

        if args[0] == "list":
            pass

        if args[0].startswith("mark"):
            pass

        app_service.save_tasks()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
