import os
import json


from task import Task


class AppService:
    def __init__(self):
        self.PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
        self.DATABASE_PATH = f"{self.PROJECT_PATH}/database.json"
        self.last_id = 0
        self.tasks = []

    def init_tasks(self) -> None:
        if not os.path.exists(self.DATABASE_PATH):
            with open(self.DATABASE_PATH, "w") as f:
                json.dump([{"last_id": 0}], f, ensure_ascii=False)
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
