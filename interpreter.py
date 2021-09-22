from tokentype import *
import expr
import operator
import environment


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


class Interpreter:
    def __init__(self):
        self.environment = environment.Environment()

    def evaluate_literal(self, expr):
        return expr.value

    def evaluate_grouping(self, expr):
        return self.evaluate(expr.expression)

    def evaluate_unary(self, expr):
        right = evaluate(expr.right)
        operator = expr.operator.type
        if unop := unary_operator.get(operator):
            return unop(right)

    def evaluate_binary(self, expr):
        left = self.evalute(expr.left)
        right = self.evaluate(expr.right)
        operator = expr.operator.type
        if binop := binary_operator.get(operator):
            return binop(left, right)
        elif operator == PLUS:
            number = (int, float)
            if isinstance(left, number) and isinstance(right, number):
                # return operator.__add__(left, right) 
                return left + right
            elif isinstance(left, str) and isinstance(right, str):
                return left + right
            else:
                print(f"left has type {type(left)} and right has type {type(right)} and they don't support PLUS")
    
    def evaluate_variable(self, expr):
        return self.environment.get(expr.name)

    def evaluate_assign(self, expr):
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name, value)
        return  value

    def evaluate(self, e):
        if isinstance(e, expr.Literal):
            return self.evaluate_literal(e)
        elif isinstance(e, expr.Grouping):
            return self.evaluate_grouping(e)
        elif isinstance(e, expr.Unary):
            return self.evaluate_unary(e)
        elif isinstance(e, expr.Binary):
            return self.evaluate_binary(e)
        elif isinstance(e, expr.Variable):
            return self.evaluate_variable(e)
        elif isinstance(e, expr.Assign):
            return self.evaluate_assign(e)

    def execute_block(self, statements, environment):
        previous_environment = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            this.environment = previous_environment

    def execute(self, statement):
        pass