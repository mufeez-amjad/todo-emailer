from typing import List, Union

from task_email import Emailer
from models import Task, Checklist

TASK_LISTS = ["Home", "School/Coop", "Side Projects"]


class ToDo:
    def __init__(self):
        self.emailer = Emailer()

    def send_emails(self):
        self.emailer.send_emails()

    def add_task(self, task: Union[Task, Checklist]):
        self.emailer.add_email(task.generate_email())

    def get_tasks(self):
        tasks: List[Union[Task, Checklist]] = []
        emails = [task.generate_email() for task in tasks]
        self.emailer.emails = emails


if __name__ == "__main__":
    todo = ToDo()
    tasks = []

    for task in tasks:
        todo.add_task(task)

    todo.send_emails()
