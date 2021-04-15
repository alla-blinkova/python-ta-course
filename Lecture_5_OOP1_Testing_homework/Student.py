class Student:
    __slots__ = ["last_name", "first_name"]

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None
