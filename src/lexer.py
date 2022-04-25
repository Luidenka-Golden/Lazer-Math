from sre_parse import WHITESPACE
from tokens import Token, TokenType

ABC = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

class Lexer:
    def __init__(self, text: str) -> None:
        self.raw_text = text
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char.isdigit():
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MUL)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIV)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Name Error: Unknown Symbol '{self.current_char}'\n")

    def generate_number(self) -> Token:
        number = self.current_char
        hv_dot = False
        self.advance()
        while self.current_char != None and self.current_char in "1234567890.":
            if self.current_char == '.':
                if hv_dot:
                    raise Exception(f"Name Error: Unknown Symbol '{self.current_char}'\n")
                hv_dot = True
            number += self.current_char
            self.advance()
        
        if number.startswith('.'):
            number = '0' + number
        if number.endswith('.'):
            number += '0'
        
        return Token(TokenType.NUMBER, float(number))