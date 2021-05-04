from datetime import datetime, timedelta


class Homework:
    __slots__ = ["text", "created", "deadline"]

    def __init__(self, text, days_count):
        self.text = text
        self.created = datetime.now()
        self.deadline = self.created + timedelta(days=days_count)

    def is_active(self):
        return datetime.now() < self.deadline
