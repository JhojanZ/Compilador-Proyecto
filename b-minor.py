"""
usage: bminor.py [-h] [-v] [--scan | --dot | --sym] [filename]

Compilador para B-Minor programas

options:
    -h, --help            Show this help message and exit
    -v, --version         Show version information and exit

Opciones de formato:
    --scan                Run the lexer and show tokens
    --dot                 Generate a DOT file for the AST
    --sym                 Show the symbol table
    [filename]            The source file to compile

"""

#argparse

import argparse
import sys

from rich import print
from lexer import tokenize
from errors import error

# Muestra un mensaje de ayuda cuando no se proporciona ningun argumento extra
def usage(exit_code=1):
    print("[blue]Usage: bminor.py --option filename[/blue]", file=sys.stderr)
    sys.exit(exit_code)

# Función para analizar los argumentos de la línea de comandos
def parse_args():
    cli = argparse.ArgumentParser(
        prog="bminor.py",
        description="Compilador para B-Minor"
    )
    cli.add_argument("-v", "--version", action="version", version="0.1")

    fgroup = cli.add_argument_group("Formateado opciones")
    cli.add_argument("filename", 
                     type=str,
                     nargs="?",
                     help="The source file to compile")

    mutex = fgroup.add_mutually_exclusive_group()
    mutex.add_argument("--scan", action="store_true", default=False, help="Run the lexer and show tokens")


    return cli.parse_args()

# Función principal
def main():
    if(len(sys.argv) == 1):
        usage()

    if(len(sys.argv) > 3):
        error("Cantidad de argumentos no válida.")
        usage()
        return  

    args = parse_args()

    if args.filename:
        fname = args.filename

        with open(fname, encoding="utf-8") as file:
            source = file.read()
        
        if args.scan:
            flex = fname.split(".")[0] + ".lex"
            tokenize(source)
            

if __name__ == "__main__":
    main()