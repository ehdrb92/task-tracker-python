import os
import json


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
