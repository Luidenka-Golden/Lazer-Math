from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    LPAREN = 5
    RPAREN = 6
    IDENTIFIER = 7

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self) -> str:
        return self.type.name + (f':{self.value}' if self.value != None else '')