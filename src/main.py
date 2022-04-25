from _parser import Parser
from interpreter import Interpreter
from lexer import Lexer

while True:
    try:
        text = input('>>> ')
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens, text)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)