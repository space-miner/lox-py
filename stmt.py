import expr


class Stmt(object):
    pass


class Expression(Stmt):
    def __init__(self, expression):
        self.expression = expression
       

class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression