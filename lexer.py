import sly

from errors import error

class Lexer(sly.Lexer):
    tokens = {
        'ARRAY', 'AUTO', 'BOOLEAN', 'CHAR', 'ELSE', 'FALSE', 'FLOAT', 'FOR', 'FUNCTION',
        'IF', 'INTEGER', 'RETURN', 'STRING', 'TRUE', 'VOID', 'WHILE',

        # Operators
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NEQ', 'LAND', 'LOR', 'INC', 'DEC',

        # Other simbols
        'ID', 'INTEGER_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL', 'CHAR_LITERAL',
    }

    literals = '+-*/%=()[]{};,:'

    ignore = ' \t\r'

    ignore_cppcomments = r'//.*'

    @_(r'\n+')
    def ignore_newlines(self, t):
        self.lineno += t.value.count('\n')

    ID = r'[_a-zA-Z_]\w*'