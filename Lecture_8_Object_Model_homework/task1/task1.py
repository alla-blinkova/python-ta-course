class KeyValueStorage:
    def __init__(self, file_path):
        with open(file_path, mode="r") as file_input:
            for line in file_input:
                line_parts = line.split("=")
                if not line_parts[0].isidentifier():
                    raise ValueError("Wrong attribute name")
                if not line_parts[0] in dir(self):
                    self.__dict__[line_parts[0]] = KeyValueStorage.convert_value(
                        line_parts[1]
                    )

    def __getitem__(self, item):
        return self.__dict__[item]

    @staticmethod
    def convert_value(value):
        value_strip = value.strip()
        try:
            return int(value_strip)
        except ValueError:
            return value_strip
