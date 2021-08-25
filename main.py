from expr import *
from tokentype import *
from token import Token


if __name__ == "__main__":
    left = Unary(Token(MINUS, "-", None, 1), Literal(123))
    right = Grouping(Literal(45.67))
    expr = Binary(left, Token(STAR, "*", None, 1), right)
    print(expr)

