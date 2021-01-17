from datetime import datetime
from typing import List, Union
from .task import Task

class Checklist(Task):
    def __init__(
        self, 
        task: str, 
        list_name: str, 
        tags: List[str], 
        start: Union[str, datetime], 
        due: Union[str, datetime],
        tasks = List[Task]
    ) -> None:
        super().__init__(task, list_name, tags, start, due)
        self.tasks = []
    
    def generate_email(self):
        tasks = [task.generate_email(False) for task in self.tasks]
        body = '\n'.join(tasks)
        
        email = super().generate_email()
        email.body = body

        return email
    