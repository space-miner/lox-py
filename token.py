class Token:

    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line


    def __str__(self):
        return self.lexeme


    def __repr__(self):
        return f"Token {self.__dict__}"
