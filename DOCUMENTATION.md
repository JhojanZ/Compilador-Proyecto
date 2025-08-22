# Documentación del Proyecto Compilador B-Minor

## Resumen del Proyecto

Este proyecto es un compilador para el lenguaje de programación B-Minor. Incluye un analizador léxico (lexer), manejo de errores y una interfaz de línea de comandos para compilar y analizar archivos fuente de B-Minor. El proyecto está implementado en Python y utiliza la librería [SLY](https://github.com/dabeaz/sly) para el análisis léxico y [Rich](https://github.com/Textualize/rich) para la salida formateada en consola.


### Archivos Principales

- `b-minor.py`: Punto de entrada principal. Maneja los argumentos de la CLI y orquesta los pasos de compilación.
- `lexer.py`: Implementa el analizador léxico (lexer) para B-Minor usando SLY.
- `errors.py`: Utilidades para el reporte de errores usando Rich.
- `test.py`: Ejecutor de pruebas simple para el lexer.
- `sieve.bminor`: Archivo fuente de ejemplo en B-Minor.
- `README.md`: Descripción del proyecto e instrucciones de uso.

---

## Estructura del Lenguaje B-Minor


### Palabras Reservadas

- `array`, `auto`, `boolean`, `char`, `else`, `false`, `float`, `for`, `function`, `if`, `integer`, `return`, `string`, `true`, `void`, `while`, `do`, `print`, `assign`
  
## Tabla de Palabras Reservadas

| Palabra   | Token      | Función/Propósito                | Patrón Regex                |
|-----------|------------|--------------------------|----------------------|
| array     | ARRAY      | Declaración de tipo array        | `array` |
| auto      | AUTO       | Inferencia de tipo               | `auto` |
| boolean   | BOOLEAN    | Declaración de tipo booleano     | `boolean` |
| char      | CHAR       | Declaración de tipo char         | `char` |
| else      | ELSE       | Rama else en control de flujo    | `else` |
| false     | FALSE      | Literal booleano falso           | `false` |
| float     | FLOAT      | Declaración de tipo flotante     | `float` |
| for       | FOR        | Bucle for                        | `for` |
| function  | FUNCTION   | Declaración de función           | `function` |
| if        | IF         | Rama if en control de flujo      | `if` |
| integer   | INTEGER    | Declaración de tipo entero       | `integer` |
| return    | RETURN     | Sentencia de retorno             | `return` |
| string    | STRING     | Declaración de tipo cadena       | `string` |
| true      | TRUE       | Literal booleano verdadero       | `true` |
| void      | VOID       | Declaración de tipo void         | `void` |
| while     | WHILE      | Bucle while                      | `while` |
| do        | DO         | Bucle do-while                   | `do` |
| print     | PRINT      | Sentencia de impresión           | `print` |


### Operadores

- Aritméticos: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- Asignación: `=`
- Comparación: `<`, `<=`, `>`, `>=`, `==`, `!=`
- Lógicos: `&&`, `||`


### Literales

- Entero: `0`, `42`, `1234`
- Flotante: `3.14`, `0.001`, `2.5e10`
- Cadena: `"Hola, mundo!"`
- Carácter: `'a'`, `'\n'`, `'0x41'`


### Identificadores

- Deben comenzar con una letra o guion bajo, seguidos de letras, dígitos o guiones bajos.


### Símbolos

- Paréntesis: `(`, `)`
- Corchetes: `[`, `]`
- Llaves: `{`, `}`
- Punto y coma: `;`
- Dos puntos: `:`
- Coma: `,`

---

## Documentación de Archivos


### b-minor.py

- Maneja los argumentos de línea de comandos usando `argparse`.
- Soporta opciones:
  - `--scan`: Ejecuta el lexer y muestra los tokens.
  - `--dot`: Genera archivo DOT para el AST (no implementado).
  - `--sym`: Muestra la tabla de símbolos (no implementado).
  - `-v`, `--version`: Muestra información de versión.
  - `-h`, `--help`: Muestra el mensaje de ayuda.
- Lee el archivo fuente y pasa el contenido al lexer si se usa `--scan`.


### lexer.py

- Define la clase `Lexer` (hereda de `sly.Lexer`).
- Especifica los tokens, literales, caracteres ignorados y comentarios.
- Maneja los saltos de línea y el conteo de líneas.
- Reconoce palabras reservadas e identificadores.
- Define patrones regex para operadores y literales.
- Proporciona la función `tokenize(txt)` para imprimir los tokens en una tabla Rich.


### errors.py

- Proporciona reporte de errores mediante la consola Rich.
- Funciones:
  - `error(message, lineno=None)`: Imprime mensaje de error formateado.
  - `get_error_count()`: Retorna el número de errores detectados.
  - `reset_errors()`: Reinicia el contador de errores.


### test.py

- Importa el lexer y ejecuta `tokenize()` en un fragmento de código de ejemplo en B-Minor.

---


## Ejemplo de Código B-Minor

```bminor
if (x <= 10) {
  print ("hola");
  x++;
}
```

---


## Uso

### Ejecutar el Lexer y Mostrar Tokens

```powershell
python b-minor.py --scan sieve.bminor
```

### Ejecutar Prueba

```powershell
python test.py
```

---


## Dependencias

- Python 3.x
- SLY (`pip install sly`)
- Rich (`pip install rich`)

---


## Trabajo Futuro

- Implementar la generación de AST (opción `--dot`)
- Implementar la visualización de la tabla de símbolos (opción `--sym`)
- Agregar soporte de advertencias en `errors.py`
- Expandir las características del lenguaje y el manejo de errores

---


## Autores

- 
