
import os
import sys
from lexer import tokenize
from errors import get_error_count, reset_errors
from rich import print
import argparse

# Carpeta donde se almacenaran los casos de prueba
TEST_DIR = "Test"

# Función para ejecutar un caso de prueba
def run_test(file_path, show_table=False):
    with open(file_path, encoding="utf-8") as f:
        source = f.read()
    
    # Reiniciamos el contador de errores a 0
    reset_errors()


    print(f"[bold]Archivo:[/bold] {file_path}")
    if show_table:
        # Mostramos la tabla de tokens si se coloco el argumento --show-table
        tokenize(source)
    else:
        from lexer import Lexer
        lex = Lexer()
        for _ in lex.tokenize(source):
            pass  # Solo tokeniza, no imprime nada
        
    errors = get_error_count()
    if errors == 0:
        print("[bold green]ACCEPTED[/bold green]")
    else:
        print("[bold red]ERROR[/bold red]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run B-Minor lexer tests")
    parser.add_argument('--show-table', action='store_true', default=False, help='Mostrar la tabla de tokens')
    args = parser.parse_args()

    test_files = [f for f in os.listdir(TEST_DIR) if f.endswith(".bminor")]
    for test_file in sorted(test_files):
        run_test(os.path.join(TEST_DIR, test_file), show_table=args.show_table)
