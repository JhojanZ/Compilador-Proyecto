# Error handling in Compilator B-Minor

from rich import print

_error_detected = 0
def error(message, line=None):
    global _error_detected
    if line:
        print(f"[red]Error on line {line}: {message}[/red]")
    else:
        print(f"[red]Error: {message}[/red]")
    _error_detected += 1

def error_detected():
    return _error_detected

def clear_errors():
    global _error_detected
    _error_detected = 0
    



error(    "This is a generic error message. Please provide more details.", line=42)