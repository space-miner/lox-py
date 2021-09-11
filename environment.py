class Environment:
    def __init__(self):
        self.values = {}

    def define(identifier, value):
        self.values[identifier] = value

    def get(identifier):
        value = self.values.get(identifier)
        if not value:
            print(f"{identifier} was not found")
        elif value:
            return value