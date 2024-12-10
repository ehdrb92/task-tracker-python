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
            task = Task(id=int(args[1]), description=args[2], updated_at=datetime.now())
            app_service.update_task_description(task)

        if args[0] == "delete":
            app_service.delete_task(int(args[1]))

        if args[0] == "list":
            if len(args) == 1:
                app_service.get_tasks()
            else:
                task = Task(status=args[1])
                app_service.get_tasks_with_filter(task.status)

        if args[0].startswith("mark"):
            status = args[0][5:]
            task = Task(id=int(args[1]), status=status, updated_at=datetime.now())
            app_service.update_task_status(task)

        app_service.save_tasks()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
