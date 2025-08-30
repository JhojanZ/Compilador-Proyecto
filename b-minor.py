"""
uso: bminor.py [-h] [-v] [--scan | --dot | --sym] [filename]

Compilador para programas B-Minor

opciones:
    -h, --help            Muestra este mensaje de ayuda y sale
    -v, --version         Muestra la información de versión y sale

Opciones de formato:
    --scan                Ejecuta el lexer y muestra los tokens
    --dot                 Genera un archivo DOT para el AST
    --sym                 Muestra la tabla de símbolos
    [filename]            El archivo fuente a compilar

"""

#argparse

import argparse
import ast
import sys

from rich import print
from lexer import tokenize
from errors import error
from parser import parse
from ast_utils import print_astt

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

    def check_invalid_args():
        valid_options = {"--scan", "--dot", "--sym", "-h", "--help", "-v", "--version"}
        args = sys.argv[1:]
        for arg in args:
            if arg.startswith("-") and arg not in valid_options:
                error(f"Argumento no válido: {arg}")
                return

    check_invalid_args()

    args = parse_args()
    

    if args.filename:
        fname = args.filename
        # Validar extensión .bminor
        if not fname.endswith('.bminor'):
            error(f"Solo se permiten archivos con extensión .bminor: {fname}")
            usage()
            return

        with open(fname, encoding="utf-8") as file:
            source = file.read()
        
        if args.scan:
            flex = fname.split(".")[0] + ".lex"
            tokenize(source)

            program_ast = parse(source)
            print_astt(program_ast)

            from ast_to_png import ast_to_graph
            import os
            g = ast_to_graph(program_ast)
            g.render("ast", cleanup=True)  # genera ast.png
            os.startfile("ast.png")
            

if __name__ == "__main__":
    main()