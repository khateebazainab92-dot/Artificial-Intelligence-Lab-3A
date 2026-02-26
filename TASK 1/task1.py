import ast
import operator

# Supported operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def evaluate(node):
    if isinstance(node, ast.Num):  # numbers
        return node.n
    
    elif isinstance(node, ast.BinOp):  # binary operations
        left = evaluate(node.left)
        right = evaluate(node.right)
        return operators[type(node.op)](left, right)
    
    elif isinstance(node, ast.UnaryOp):  # negative numbers
        return operators[type(node.op)](evaluate(node.operand))
    
    else:
        raise TypeError("Unsupported expression")

def calculate(expression):
    # Replace user-friendly symbols
    expression = expression.replace('×', '*').replace('÷', '/')
    
    parsed = ast.parse(expression, mode='eval')
    return evaluate(parsed.body)

# Main program loop
while True:
    try:
        expr = input("Enter expression (or 'quit' to exit): ")
        
        if expr.lower() == 'quit':
            break
        
        result = calculate(expr)
        print("Result:", result)
    
    except Exception as e:
        print("Error:", e)