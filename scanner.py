from tokentype import *
from token import Token


whitespace = set(" \r\t\n")


digits = set("1234567890")


symbols = {
    '(': LEFT_PAREN,
    ')': RIGHT_PAREN,
    '[': LEFT_BRACE,
    ']': RIGHT_BRACE,
    ',': COMMA,
    '.': DOT,
    '-': MINUS,
    '+': PLUS,
    ';': SEMICOLON,
    '/': SLASH,
    '*': STAR
}


relations = {
    '!': BANG,
    "!=": BANG_EQUAL,
    '=': EQUAL,
    "==": EQUAL_EQUAL,
    '>': GREATER,
    ">=": GREATER_EQUAL,
    '<': LESS,
    "<=": LESS_EQUAL
}


keywords = {
    "and": AND,
    "class": CLASS,
    "else": ELSE,
    "false": FALSE,
    "for": FOR,
    "fun": FUN,
    "if": IF,
    "nil": NIL,
    "or": OR,
    "print": PRINT,
    "return": RETURN,
    "super": SUPER,
    "this": THIS,
    "true": TRUE,
    "var": VAR,
    "while": WHILE
}


class Scanner:

    def __init__(self, source, token_list=[]):
        self.source = open(source, 'r').read()
        self.token_list = token_list
        self.start = 0
        self.current = 0
        self.line = 1


    def scan_tokens(self):
        while self.is_at_end() == False:
            self.start = self.current
            self.scan_token()
        # eof_token = Token(EOF, '', null, line)
        # self.token_list.append(eof_token)
        self.add_token(EOF)
        return self.token_list


    def is_at_end(self):
        return self.current >= len(self.source)


    def scan_token(self):
        ch = self.advance()
        if ch in symbols:
            token_type = symbols[ch]
            self.add_token(token_type)
        elif ch in relations:
            peek = self.peek()
            if peek == '=':
                self.advance()
                token_type = relations[ch+peek]
            elif peek != '=':
                token_type = relations[ch]
            self.add_token(token_type)
        elif ch in whitespace:
            if ch == '\n':
                self.line += 1
        elif ch == '"':
            self.string()
        elif ch.isdigit():
            self.number()
        elif ch.isalpha() or ch == '_':
            self.identifier()
        else:
            print(f"line: {self.line}\tunexpected character: {ch}")


    def advance(self):
        ch = self.source[self.current]
        self.current += 1
        return ch


    def add_token(self, token_type, literal=None):
        line = self.line
        lexeme = self.source[self.start:self.current]
        token = Token(token_type, lexeme, literal, line)
        self.token_list.append(token)
    

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]


    def string(self):
        while self.is_at_end() == False and self.peek() != '"':
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        self.advance()   # closing " 
        literal = self.source[self.start:self.current]
        self.add_token(STRING, literal)


    def number(self):
        is_decimal = False
        while self.peek().isdigit():
            self.advance()
        if self.peek() == '.':
            is_decimal = True
            self.advance()
        while self.peek().isdigit():
            self.advance()
        string_of_number = self.source[self.start:self.current]
        literal = float(string_of_number) if is_decimal else int(string_of_number)
        self.add_token(NUMBER, literal)


    def identifier(self):
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()
        lexeme = self.source[self.start:self.current]
        token_type = keywords.get(lexeme, IDENTIFIER)
        self.add_token(token_type)
