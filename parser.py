from tokentype import *
import expr


literals = {
    "FALSE": False,
    "TRUE": True,
    "NIL": None
    }


class Parser():

    def __init__(self, token_list, current=0):
        self.token_list = token_list
        self.current = current


    def expression(self):
        return self.equality()


    def equality(self):
        left = self.comparison()
        typ = self.peek().type
        while typ in [BANG_EQUAL, EQUAL_EQUAL]:
            operator = self.advance()
            right = self.comparison()
            left = expr.Binary(left, operator, right)
        return left


    def comparison(self):
        left = self.term()
        typ = self.peek().type
        while typ in [GREATER, GREAT_EQUAL, LESS, LESS_EQUAL]:
            operator = self.advance()
            right = self.term()
            left = expr.Binary(left, operator, right)
        return left

    
    def term(self):
        left = self.factor()
        typ = self.peek().type
        while typ in [MINUS, PLUS]:
            operator = self.advance()
            right = self.factor()
            left = expr.Binary(left, operator, right)
        return left

    
    def factor(self):
        left = self.unary()
        typ = self.peek().type
        while typ in [SLASH, STAR]:
            operator = self.advance()
            right = self.unary()
            left = expr.Binary(left, operator, right)
        return left

    
    def unary(self):
        typ = self.peek().type
        if typ in [BANG, MINUS]:
            operator = self.advance()
            right = self.unary()
            return expr.Unary(operator, right)
        return primary()

    
    def primary(self):
        typ = self.peek().type
        if typ in literals:
            value = literal[typ]
            return expr.Literal.(value)
        elif typ in [NUMBER, STRING]:
            token = advance()
            return expr.Literal(token.literal)
        elif typ == LEFT_PAREN:
            exp = expression()
            consume(RIGHT_PAREN)
            return expr.Literal(exp)

        
    def peek(self):
        return self.token_list[self.current]

    
    def is_at_end(self):
        return self.peek().type == EOF
    
    
    def advance(self):
        if not self.is_at_end():
            token = self.peek()
            self.current += 1
            return token


    def consume(self, typ):
        if self.peek().type == typ:
            return self.advance()
        else:
            token = self.peek()
            print(f"line: {token.line}\t{token.type} != {typ}")
