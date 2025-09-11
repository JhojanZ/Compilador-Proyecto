from dataclasses import dataclass, field
from multimethod import multimeta, multimethod
from typing      import List, Union
import rich

# =====================================================================
# Clases Abstractas
# =====================================================================
class Visitor(metaclass=multimeta):
    pass

@dataclass
class Node:
    def accept(self, v: Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

    def pretty(self, indent=0):
        console = rich.console.Console()
        console.print("\n[bold yellow]Árbol de sintaxis (AST) en consola:[/bold yellow]")
        #TO DO: Implementarl el ast_utils aqui para que no se llame como modulo
        from ast_utils import print_astt
        print_astt(self)

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

# =====================================================================
# Definiciones
# =====================================================================
@dataclass
class Program(Statement):
    body: List[Statement] = field(default_factory=list)


# Expresiones

@dataclass
class BinOper(Expression):
    oper : str
    left : Expression
    right: Expression

@dataclass
class UnaryOper(Expression):
    oper : str
    expr : Expression

@dataclass
class Literal(Expression):
    value : Union[int, float, str, bool]
    type  : str = None

@dataclass
class Integer(Literal):
    value : int

    def __post_init__(self):
        assert isinstance(self.value, int), "Value debe ser un 'integer'"
        self.type = 'integer'
        
@dataclass
class Float(Literal):
    value : float

    def __post_init__(self):
        assert isinstance(self.value, float), "Value debe ser un 'float'"
        self.type = 'float'

@dataclass
class Boolean(Literal):
    value : bool

    def __post_init__(self):
        assert isinstance(self.value, bool), "Value debe ser un 'boolean'"
        self.type = 'boolean'

# =====================================================================
# Declaraciones y asignaciones
# =====================================================================

@dataclass
class Decl(Statement):
    name : str
    type : str
    value: Expression = None   # opcional, si no hay inicialización

@dataclass
class Assign(Statement):
    name : str
    value: Expression

# =====================================================================
# Visitor/Interpreter para ejecutar asignaciones y declaraciones
# =====================================================================
class Interpreter(Visitor):
    def __init__(self):
        self.symbols = {}

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Program(self, node):
        for stmt in node.body:
            self.visit(stmt)

    def visit_Decl(self, node):
        value = self.visit(node.value) if node.value else None
        self.symbols[node.name] = value
        return value

    def visit_Assign(self, node):
        value = self.visit(node.value)
        self.symbols[node.name] = value
        return value

    def visit_Integer(self, node):
        return node.value

    def visit_Float(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_Literal(self, node):
        return node.value

    def visit_BinOper(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.oper == '+':
            return left + right
        elif node.oper == '-':
            return left - right
        elif node.oper == '*':
            return left * right
        elif node.oper == '/':
            return left / right
        elif node.oper == '%':
            return left % right
        elif node.oper == '==':
            return left == right
        elif node.oper == '!=':
            return left != right
        elif node.oper == '<':
            return left < right
        elif node.oper == '<=':
            return left <= right
        elif node.oper == '>':
            return left > right
        elif node.oper == '>=':
            return left >= right
        elif node.oper == '&&':
            return left and right
        elif node.oper == '||':
            return left or right
        else:
            raise Exception(f'Operador binario no soportado: {node.oper}')

    def visit_UnaryOper(self, node):
        expr = self.visit(node.expr)
        if node.oper == '-':
            return -expr
        elif node.oper == '!':
            return not expr
        else:
            raise Exception(f'Operador unario no soportado: {node.oper}')

# =====================================================================
# Control de flujo
# =====================================================================

@dataclass
class If(Statement):
    cond        : Expression
    then_branch : Statement
    else_branch : Statement = None   # opcional

@dataclass
class For(Statement):
    init   : Expression
    cond   : Expression
    update : Expression
    body   : Statement
    
@dataclass
class Block(Statement):
    stmts: List[Statement] = field(default_factory=list)

@dataclass
class Print(Statement):
    values: List[Expression] = field(default_factory=list)

@dataclass
class Return(Statement):
    value: Expression = None
