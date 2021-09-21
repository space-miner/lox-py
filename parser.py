from tokentype import *
import expr
import stmt


literals = {
    FALSE: False,
    TRUE: True,
    NIL: None
}


class Parser():

    def __init__(self, token_list, current=0):
        self.token_list = token_list
        self.current = current


    def parse(self):
        statement_list = []
        while not self.is_at_end():
            stmt = self.declaration()
            statement_list.append(stmt)
        self.consume(EOF)
        return statement_list


    def declaration(self):
        typ = self.peek().type
        if typ == VAR:
            return self.variable_declaration()
        else:
            return self.statement()


    def variable_declaration(self):
        self.consume(VAR)
        ident = self.advance()
        expr = None
        typ = self.peek().type
        if typ == EQUAL:
            self.consume(EQUAL)
            expr = self.expression()
        self.consume(SEMICOLON)
        return stmt.Var(ident, expr)

    def statement(self):
        typ = self.peek().type
        if typ == PRINT:
            return self.print_statement()
        else:
            return self.expression_statement()


    def print_statement(self):
        self.consume(PRINT)
        expr = self.expression()
        self.consume(SEMICOLON)
        return stmt.Print(expr)


    def expression_statement(self):
        expr = self.expression()
        self.consume(SEMICOLON)
        return stmt.Expression(expr)


    def expression(self):
        return self.assignment()


    def assignment(self):
        expr = self.equality()
        typ = self.peek().type
        if typ == EQUAL:
            value = assignment()
            if isinstance(expr, expr.Variable):
                name = expr.name
                return expr.Assign(name, value)
        return expr


    def equality(self):
        left = self.comparison()
        typ = self.peek().type
        while typ in [BANG_EQUAL, EQUAL_EQUAL]:
            operator = self.advance()
            right = self.comparison()
            left = expr.Binary(left, operator, right)
            typ = self.peek().type
        return left


    def comparison(self):
        left = self.term()
        typ = self.peek().type
        while typ in [GREATER, GREATER_EQUAL, LESS, LESS_EQUAL]:
            operator = self.advance()
            right = self.term()
            left = expr.Binary(left, operator, right)
            typ = self.peek().type
        return left

    
    def term(self):
        left = self.factor()
        typ = self.peek().type
        while typ in [MINUS, PLUS]:
            operator = self.advance()
            right = self.factor()
            left = expr.Binary(left, operator, right)
            typ = self.peek().type
        return left

    
    def factor(self):
        left = self.unary()
        typ = self.peek().type
        while typ in [SLASH, STAR]:
            operator = self.advance()
            right = self.unary()
            left = expr.Binary(left, operator, right)
            typ = self.peek().type
        return left

    
    def unary(self):
        typ = self.peek().type
        if typ in [BANG, MINUS]:
            operator = self.advance()
            right = self.unary()
            return expr.Unary(operator, right)
        return self.primary()

    
    def primary(self):
        typ = self.peek().type
        if typ in literals:
            value = literals[typ]
            self.advance()
            return expr.Literal(value)
        elif typ in [NUMBER, STRING]:
            token = self.advance()
            return expr.Literal(token.literal)
        elif typ == LEFT_PAREN:
            expr = expression()
            consume(RIGHT_PAREN)
            return expr.Literal(expr)
        elif typ == IDENTIFIER:
            token = self.advance()
            return expr.Variable(token)

        
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
            print(token)
            print(f"line: {token.line}\t expected {typ} but got {token.type}")
