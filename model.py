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
