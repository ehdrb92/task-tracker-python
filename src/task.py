from dataclasses import dataclass
from datetime import datetime


from task_status import TaskStatus


@dataclass
class Task:
    id: int
    decription: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
