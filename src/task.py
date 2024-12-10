from dataclasses import dataclass
from datetime import datetime


from task_status import TaskStatus


@dataclass
class Task:
    id: int
    decription: str
    created_at: datetime
    updated_at: datetime
    status: TaskStatus = 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["todo", "in-progress", "done"]:
            raise ValueError("status must 'todo' or 'in-progress' or 'done'")
        if value == "todo":
            self._status = 1
        if value == "in-progress":
            self._status = 2
        if value == "done":
            self._status = 3

    def to_dict(self):
        return {
            "id": self.id,
            "decription": self.decription,
            "status": self._status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
