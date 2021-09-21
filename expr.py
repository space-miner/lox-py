from tokentype import *
from token import Token


class Expr(object):
    pass


class Assign(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"[{self.name} = {self.value}]"


class Binary(Expr):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"[{str(self.left)} {self.operator} {str(self.right)}]"


class Grouping(Expr):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"[({str(self.expression)})]"


class Literal(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"[{str(self.value)}]"


class Unary(Expr):
    def __init__(self, operator, value):
        self.operator = operator
        self.value = value

    def __str__(self):
       return f"[{self.operator} {str(self.value)}]"


class Variable(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"[{self.name}]"