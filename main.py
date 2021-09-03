import sys
from expr import *
from tokentype import *
from token import Token
from scanner import Scanner
from parser import Parser
from interpreter import *


if __name__ == "__main__":
    lox_file = sys.argv[1]
    print(f"interpreting: {lox_file}")
    S = Scanner(lox_file)
    tokens = S.scan_tokens()
    P = Parser(tokens)
    top_expr = P.parse()
    print(interpret(top_expr))
