from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self) -> str:
        return f'{self.value}'

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f'({self.node_a}+{self.node_b})'

@dataclass
class SubNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f'({self.node_a}-{self.node_b})'

@dataclass
class MulNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f'({self.node_a}*{self.node_b})'

@dataclass
class DivNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f'({self.node_a}/{self.node_b})'

@dataclass
class PosNode:
    node: any

    def __repr__(self) -> str:
        return f'(+{self.node})'

@dataclass
class NegNode:
    node: any

    def __repr__(self) -> str:
        return f'(-{self.node})'