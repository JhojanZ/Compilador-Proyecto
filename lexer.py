import sly

from errors import error

class Lexer(sly.Lexer):
    tokens = {
        'ARRAY', 'AUTO', 'BOOLEAN', 'CHAR', 'ELSE', 'FALSE', 'FLOAT', 'FOR', 'FUNCTION',
        'IF', 'INTEGER', 'RETURN', 'STRING', 'TRUE', 'VOID', 'WHILE', 'ASSIGN'

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
    LT  = r'<'
    LE  = r'<='
    GT  = r'>'
    GE  = r'>='
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
    STRING_LITERAL = r'"([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))*"'
    CHAR_LITERAL = r"([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))'"
