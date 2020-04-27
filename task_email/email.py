EMAIL_SUBJECT_PREFIX = 'todo:'


class Email:
    def __init__(self, subject: str, body: str, options: dict):
        self.subject = f'{EMAIL_SUBJECT_PREFIX} {subject}'
        self.body = body
        self.apply_options(options)

    def apply_options(self, options: dict):
        def get_formatted_date(date) -> str:
            # ex. 15-05-20 (May 15 2020)
            formatted_date = date.strftime('%-m-%-d-%-y')

            if date.hour or date.minute:  
                formatted_date += ' ' + date.strftime('%-I%m%p')

            return formatted_date

        formatted_options = []

        start_date = options.get('start_date')
        due_date = options.get('due_date')
        priority = options.get('priority')
        list_name = options.get('list')
        tags = options.get('tags')

        if start_date:
            formatted_options.append(f'start({get_formatted_date(start_date)})')

        if due_date:
            formatted_options.append(f'due({get_formatted_date(due_date)})')

        if priority:
            priority_symbol = priority * '!'
            formatted_options.append(f'priority({priority_symbol})')

        if list_name:
            formatted_options.append(f'list({list_name})')

        if tags:
            tags_list = ','.join(tags)
            formatted_options.append(f'tag({tags_list})')

        self.subject += ' ' + ' '.join(formatted_options)
