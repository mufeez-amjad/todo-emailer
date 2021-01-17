EMAIL_SUBJECT_PREFIX = 'todo:'

class Email:
    def __init__(self, subject: str, body: str = ''):
        self.subject = f'{EMAIL_SUBJECT_PREFIX} {subject}'
        self.body = body

    def __str__(self):
        return f'<Email: {self.subject}>'