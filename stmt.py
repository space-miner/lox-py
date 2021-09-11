import expr


class Stmt(object):
    pass


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
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f"[var {identifier} = {expression}]"