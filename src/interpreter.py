from nodes import *
from values import *

class Interpreter:
    def visit(self, node):
        method_name = f'visit{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visitNumberNode(self, node):
        return Number(node.value)

    def visitAddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visitSubNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visitMulNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visitDivNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except ZeroDivisionError:
            raise Exception("MathError: Can't divide by zero")
        except:
            raise Exception("MathError: Runtime math error")

    def visitPosNode(self, node):
        return self.visit(node.node)

    def visitNegNode(self, node):
        return Number(-(self.visit(node.node)).value)