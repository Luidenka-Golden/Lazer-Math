from tokens import TokenType, Token
from nodes import *

class Parser:
    def __init__(self, tokens, raw_text) -> None:
        self.tokens = iter(tokens)
        self.raw_text = raw_text
        self.advance()

    def raise_error(self):
        raise Exception(f"Name Error: Invalid Syntax {self.current_token}\n")

    def advance(self):
        try:
            self.current_token: Token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expr()

        if self.current_token != None:
            self.raise_error()

        return result

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MUL, TokenType.DIV):
            if self.current_token.type == TokenType.MUL:
                self.advance()
                result = MulNode(result, self.factor())
            elif self.current_token.type == TokenType.DIV:
                self.advance()
                result = DivNode(result, self.factor())
        
        return result

    def factor(self):
        token = self.current_token
        
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PosNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return NegNode(self.factor())

        self.raise_error()