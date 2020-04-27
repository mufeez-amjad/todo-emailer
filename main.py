from task_email import Email, Emailer
from dateutil.parser import parse
from typing import Dict

TASK_LISTS = ['Home', 'School/Coop', 'Side Projects']


class ToDo:
    def __init__(self):
        self.emailer = Emailer()

    def send_emails(self):
        self.emailer.send_emails()

    def get_options(self):
        options_prompt = (
            'Select which properties to add:\n'
            '\t1. Start Date\n'
            '\t2. Due Date\n'
            '\t3. Priority\n'
            '\t4. List Name\n'
            '\t5. Tag(s)\n'
        )

        selected_options = input(options_prompt)
        print()
        options = {}

        # TODO: support Action = (action, value) where action can be call, message, mail, url, visit, google
        handlers = [
            self._start_date, self._due_date, self._priority, self._list,
            self._tag
        ]

        if selected_options:
            for selected_option in selected_options.split(' '):
                index = int(selected_option) - 1
                options = handlers[index](options)
                print()

        return options

    def _start_date(self, options: Dict) -> Dict:
        try:
            full_date = parse(input('Enter the start date.\n'))
            options['start_date'] = full_date

            return options
        except ValueError:
            print('Invalid time format.\n')
            return self._start_date(options)

    def _due_date(self, options: Dict) -> Dict:
        try:
            full_date = parse(input('Enter the due date.\n'))
            options['due_date'] = full_date

            return options
        except ValueError:
            print('Invalid time format.\n')
            return self._due_date(options)

    def _priority(self, options: Dict) -> Dict:
        priority_num = int(input('Enter a priority 1-3.\n'))
        while priority_num > 3:
            priority_num = int(input('Enter a priority 1-3.\n'))

        options['priority'] = priority_num
        return options

    def _list(self, options: Dict) -> Dict:
        list_choice = input('Enter the list to add to this task to.\n')
        while list_choice not in TASK_LISTS:
            list_choice = input('Enter the list to add to this task to.\n')

        options['list'] = list_choice
        return options

    def _tag(self, options: Dict) -> Dict:
        tags = input('Enter tags.\n').split(' ')

        options['tags'] = tags
        return options

    def task(self):
        task = input('Enter your task.\n')
        email_subject = task

        options = self.get_options()

        email = Email(email_subject, '', options)
        self.emailer.add_email(email)

    def checklist(self):
        tasks = []
        list_name = input('Enter checklist name.\n')
        print('Enter your tasks for this list.')
        task = input()
        while task:
            tasks.append(task)
            task = input()

        options = self.get_options()

        email_subject = list_name
        email_body = '\n'.join(
            [f'{index+1}. {task}' for index, task in enumerate(tasks)]
        )
        email = Email(email_subject, email_body, options)

        self.emailer.add_email(email)


def main():
    todo = ToDo()
    prompt = (
        'Choose one on the following:\n'
        '\t1. Task\n'
        '\t2. Checklist\n'
        '\t0. Finish\n'
    )
    option = int(input(prompt))
    print()
    while option:
        if option is 1:
            todo.task()
        elif option is 2:
            todo.checklist()
        option = int(input(prompt))
        print()

    todo.send_emails()


if __name__ == '__main__':
    main()
