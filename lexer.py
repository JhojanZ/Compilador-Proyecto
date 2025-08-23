import sly

from errors import error, get_error_count

class Lexer(sly.Lexer):
    # ...existing code...

    # Regla para detectar identificadores inválidos (por ejemplo, que empiezan con dígito)
    @_(r'[0-9]+[A-Za-z_][A-Za-z0-9_]*')
    def INVALID_ID(self, t):
        error(f"Identificador inválido: '{t.value}' en la línea {t.lineno}", t.lineno)
        # No retorna el token para que no sea procesado como válido

    """
    Analizador léxico para el lenguaje B-Minor usando SLY.
    Define los tokens, palabras reservadas, operadores y literales reconocidos por el lenguaje.
    """
    # Conjunto de tokens reconocidos por el lexer
    tokens = {
        'ARRAY', 'AUTO', 'BOOLEAN', 'CHAR', 'ELSE', 'FALSE', 'FLOAT', 'FOR', 'FUNCTION',
        'IF', 'INTEGER', 'RETURN', 'STRING', 'TRUE', 'VOID', 'WHILE', 'ASSIGN', 'PRINT', 'DO',

        # Operators
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NEQ', 'LAND', 'LOR', 'INC', 'DEC',

        # Other simbols
        'ID', 'INTEGER_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL', 'CHAR_LITERAL',
    }

    

    # Caracteres literales que se reconocen directamente
    literals = '+-*/%=()[]{};,:'

    # Caracteres a ignorar (espacios, tabulaciones y retorno de carro)
    ignore = ' \t\r'

    # Ignora comentarios estilo C++ (// ...)
    ignore_cppcomments = r'//.*'
    ignore_cpplongcomment = r'/\*[\s\S]*?\*/'

    # Manejo de saltos de línea para actualizar el número de línea
    @_(r'\n+')
    def ignore_newlines(self, t):
        """
        Ignora saltos de línea y actualiza el contador de líneas.
        """
        self.lineno += t.value.count('\n')

    # Diccionario de palabras reservadas del lenguaje
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

    # Identificadores y palabras reservadas
    @_(r'[A-Za-z_][A-Za-z0-9_]*')
    def ID(self, t):
        """
        Identifica si una palabra es reservada del lenguaje o un identificador normal.
        Si la palabra está en la lista de palabras reservadas, asigna el tipo correspondiente.
        Si no, la clasifica como identificador (ID).
        """
        if t.value.lower() in self.keywords:
            t.type = self.keywords[t.value.lower()]
        else:
            t.type = 'ID'
        return t

    # ...existing code...

    # Puedes agregar reglas similares para otros tokens inválidos si lo deseas

    # ...existing code...

    # ...existing code...
    


    # Expresiones regulares para operadores
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

    # Expresiones regulares para literales
    INTEGER_LITERAL = r'0|[1-9][0-9]*'  # Números enteros
    FLOAT_LITERAL = r'(0\.[0-9]+)|([1-9][0-9]*\.[0-9]+)([eE][+-]?[0-9]+)?'  # Números flotantes
    STRING_LITERAL = r'\"([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))*\"'  # Cadenas de texto
    CHAR_LITERAL = r"\'([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))\'"  # Caracteres


def tokenize(txt):
    """
    Función auxiliar para tokenizar un texto y mostrar los tokens en una tabla usando rich.
    Args:
        txt (str): Texto fuente a analizar léxicamente.
    """
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
    if get_error_count() == 0:
        console.print(table)



if __name__ == "__main__":
    # Punto de entrada principal (no realiza ninguna acción por defecto)
    pass