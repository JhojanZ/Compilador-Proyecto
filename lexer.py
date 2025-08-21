import sly

from errors import error

class Lexer(sly.Lexer):
    tokens = {
        'ARRAY', 'AUTO', 'BOOLEAN', 'CHAR', 'ELSE', 'FALSE', 'FLOAT', 'FOR', 'FUNCTION',
        'IF', 'INTEGER', 'RETURN', 'STRING', 'TRUE', 'VOID', 'WHILE', 'ASSIGN', 'PRINT', 'DO',

        # Operators
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NEQ', 'LAND', 'LOR', 'INC', 'DEC',

        # Other simbols
        'ID', 'INTEGER_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL', 'CHAR_LITERAL',
    }

    

    literals = '+-*/%=()[]{};,:'

    ignore = ' \t\r'

    ignore_cppcomments = r'//.*'

    #manejo de saltos de linea
    @_(r'\n+')
    def ignore_newlines(self, t):
        self.lineno += t.value.count('\n')

    #las palabras reservadas se guardan en un diccionario
    # Palabras reservadas
    keywords = {
        'array': 'ARRAY',
        'auto': 'AUTO',
        'boolean': 'BOOLEAN',
        'char': 'CHAR',
        'else': 'ELSE',
        'false': 'FALSE',
        'float': 'FLOAT',
        'for': 'FOR',
        'function': 'FUNCTION',
        'if': 'IF',
        'integer': 'INTEGER',
        'return': 'RETURN',
        'string': 'STRING',
        'true': 'TRUE',
        'void': 'VOID',
        'while': 'WHILE',
        'do': 'DO',
        'print': 'PRINT'
    }

    #identifica si una palabra es reservada del lenguaje o un identificador normal.
    # Identificadores y palabras reservadas
    @_(r'[A-Za-z_][A-Za-z0-9_]*')
    def ID(self, t):
        # Si la palabra está en la lista de palabras reservadas se usara
        if t.value.lower() in self.keywords:
            t.type = self.keywords[t.value.lower()]
        else:
            # Si no, es un identificador normal
            t.type = 'ID'
        return t

    # Operadores
    LE  = r'<='
    LT  = r'<'
    GE  = r'>='
    GT  = r'>'
    EQ  = r'=='
    ASSIGN = r'='
    NEQ = r'!='
    LAND = r'&&'
    LOR  = r'\|\|'
    INC  = r'\+\+'
    DEC  = r'--'

    # Literales
    INTEGER_LITERAL = r'0|[1-9][0-9]*'
    FLOAT_LITERAL = r'(0\.[0-9]+)|([1-9][0-9]*\.[0-9]+)([eE][+-]?[0-9]+)?'
    STRING_LITERAL = r'\"([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))*\"'


    CHAR_LITERAL = r"\'([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))\'"


def tokenize(txt):
    from rich.table import Table
    from rich.console import Console

    lex = Lexer()

    table = Table(title="Tokens")
    table.add_column("type")
    table.add_column("value")
    table.add_column("line", justify="right")

    for tok in lex.tokenize(txt):
        value = tok.value if isinstance(tok.value, str) else str(tok.value)
        table.add_row(tok.type, value, str(tok.lineno))

    console = Console()
    console.print(table)


if __name__ == "__main__":
    pass