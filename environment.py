class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing = enclosing

    def define(name, value):
        self.values[name] = value

    def get(name):
        value = self.values.get(name)
        if value:
            return value
        elif not value:
            if self.enclosing:
                return self.enclosing.get(name)
            elif not self.enclosing:
                print(f"{name} was not found")

    def assign(name, value):
        lexeme = name.lexeme
        if lexeme in self.values:
            self.values[lexeme] = value
        elif lexeme not in self.values:
            if self.enclosing:
                self.enclosing.assign(name, value)
            elif not self.enclosing:
                print(f"undefined variable {lexeme}.")