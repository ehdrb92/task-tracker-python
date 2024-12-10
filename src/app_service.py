import os
import json


from task import Task


class AppService:
    def __init__(self):
        self.PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
        self.DATABASE_PATH = f"{self.PROJECT_PATH}/database.json"
        self.last_id = 1
        self.tasks = []
        self.status = ["todo", "in-progress", "done"]

    def init_tasks(self) -> None:
        if not os.path.exists(self.DATABASE_PATH):
            with open(self.DATABASE_PATH, "w") as f:
                json.dump([{"last_id": 1}], f, ensure_ascii=False)
            return

        with open(self.DATABASE_PATH, "r") as f:
            saved_data = json.load(f)
            self.last_id = saved_data[0]["last_id"]
            self.tasks = saved_data[1:]
        return

    def save_tasks(self) -> None:
        last_data = [{"last_id": self.last_id}] + self.tasks

        with open(self.DATABASE_PATH, "w") as f:
            json.dump(last_data, f, ensure_ascii=False)

    def create_task(self, task: Task) -> None:
        self.last_id += 1
        new_task = task.to_dict()
        self.tasks.append(new_task)
        print(f"Task added successfully (ID: {self.last_id})")
        return

    def get_tasks(self) -> list:
        for task in self.tasks:
            print(
                f"id: {task["id"]}, description: {task["description"]}, status: {self.status[task["status"]]}, created_at: {task["created_at"]}, updated_at: {task["updated_at"]}"
            )

    def get_tasks_with_filter(self, status_filter: int) -> list:
        for task in [task for task in self.tasks if task["status"] == status_filter]:
            print(
                f"id: {task["id"]}, description: {task["description"]}, status: {self.status[task["status"]]}, created_at: {task["created_at"]}, updated_at: {task["updated_at"]}"
            )

    def update_task_description(self, task: Task) -> None:
        update_task = task.to_dict()

        for index, task in enumerate(self.tasks):
            if task["id"] == update_task["id"]:
                self.tasks[index]["description"] = update_task["description"]
                self.tasks[index]["updated_at"] = update_task["updated_at"]
                break
        print(f"Task updated successfully (ID: {update_task["id"]})")

    def update_task_status(self, task: Task):
        update_task = task.to_dict()

        for index, task in enumerate(self.tasks):
            if task["id"] == update_task["id"]:
                self.tasks[index]["status"] = update_task["status"]
                self.tasks[index]["updated_at"] = update_task["updated_at"]
                break
        print(f"Task updated successfully (ID: {update_task["id"]})")

    def delete_task(self, id: int) -> None:
        for index, task in enumerate(self.tasks):
            if task["id"] == id:
                del self.tasks[index]
                break
        print(f"Task deleted successfully (ID: {id})")
