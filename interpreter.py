from tokentype import *
import expr
import operator


unary_operator = {
    MINUS: operator.__neg__,
    BANG: operator.__not__
}


binary_operator = {
    MINUS: operator.__sub__,
    SLASH: operator.__truediv__,
    STAR: operator.__mul__,
    GREATER: operator.__gt__,
    GREATER_EQUAL: operator.__ge__,
    LESS: operator.__lt__,
    LESS_EQUAL: operator.__le__,
    BANG_EQUAL: operator.__ne__,
    EQUAL_EQUAL: operator.__eq__
}


def interpret(e):
    if isinstance(e, expr.Literal):
        return e.value
    elif isinstance(e, expr.Grouping):
        return interpret(e.expression)
    elif isinstance(e, expr.Unary):
        right = interpret(e.right)
        operator = e.operator.type
        if unop := unary_operator.get(operator):
            return unop(right)
    elif isinstance(e, expr.Binary):
        left = interpret(e.left)
        right = interpret(e.right)
        operator = e.operator.type
        if binop := binary_operator.get(operator):
            return binop(left, right)
        elif operator == PLUS:
            number = (int, float)
            if isinstance(left, number) and isinstance(right, number):
                # return operator.__add__(left, right) 
                return left + right
            elif isinstance(left, str) and isinstance(right, str):
                return left + right
