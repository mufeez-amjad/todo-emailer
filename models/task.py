
from datetime import date, datetime
from task_email.email import Email
from typing import Literal, Union, List
from dateutil.parser import parse

class Task:
    def __init__(
        self, 
        task: str, 
        list_name: str,
        start: Union[str, datetime] = None, 
        due: Union[str, datetime] = None,
        tags: List[str] = None, 
        priority: Literal[0,1,2,3] = 0
    ) -> None:
        self.name = task
        self.list = list_name
        self.tags = tags
        self.priority = priority # FIXME: unused
        
        try:
            self.start_dt = parse(start) if isinstance(start, str) else start
            self.due_dt = parse(due) if isinstance(due, str) else due
        except ValueError:
            print('Incorrect date format.')
    
    def generate_email(self, include_options = True):
        def get_formatted_date(date: Union[date, datetime]) -> str:
            # ex. 15-05-20 (May 15 2020)
            formatted_date = date.strftime('%-m-%-d-%-y')

            if isinstance(date, datetime):  
                formatted_date += ' ' + date.strftime('%-I:%-M%p')

            return formatted_date
        
        subject = self.name

        if not include_options:
            return Email(subject)

        options = []
        if self.start_dt:
            options.append(f'start({get_formatted_date(self.start_dt)})')
        
        if self.due_dt:
            options.append(f'due({get_formatted_date(self.due_dt)})')
        
        if self.priority:
            priority_symbol = self.priority * '!'
            options.append(f'priority({priority_symbol})')
        
        if self.list:
            options.append(f'list({self.list})')

        if self.tags:
            tags_list = ','.join(self.tags)
            options.append(f'tag({tags_list})')

        subject += ' ' + ' '.join(options)
        
        return Email(subject)
