import expr


class Stmt(object):
    pass


class Block(Stmt):
    def __init__(self, statements):
        self.statements = statements

    def __str__(self):
        return f"[[ {self.statements} ]]"


class Expression(Stmt):
    def __init__(self, expression):
        self.expression = expression
       
    def __str__(self):
        return f"{self.expression}"


class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"[print({self.expression})]"


class Var(Stmt):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"[var {name} = {value}]"