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

| Palabra   | Token      | Función/Propósito                | Patrón Regex |
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
| assign    | ASSIGN     | Operador de asignación           | `=` |


### Operadores


| Operador| Token  | Función/Propósito | Patrón Regex |
|---------|--------|-------------------|--------------|
| <       | LT     | Menor que         | `<`          |
| <=      | LE     | Menor o igual que | `<=`         |
| >=      | GE     | Mayor o igual que | `>=`         |
| >       | GT     | Mayor que         | `>`          |
| ==      | EQ     | Igual             | `==`         |
| !=      | NEQ    | Diferente         | `!=`         |
| &&      | LAND   | AND logico        | `&&`         |
| ||      | LOR    | OR logico         | `\|\|`       |
| ++      | INC    | Incremento        | `\+\+`       |
| --      | DEC    | Decremento        | `--`         |
| +       | PLUS   | Suma              | `\+`         |
| -       | MINUS  | Resta             | `-`          |  
| *       | TIMES  | Multiplicacion    | `\*`         |
| /       | DIVIDE | Division          | `/`          |
| %       | MOD    | Modulo            | `%`          |

- Aritméticos: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- Asignación: `=`
- Comparación: `<`, `<=`, `>`, `>=`, `==`, `!=`
- Lógicos: `&&`, `||`


### Literales

| Tipo     | Token          | Ejemplo             | Patrón Regex                                           |
|----------|----------------|---------------------|--------------------------------------------------------|
| Entero   | INTEGER_LITERAL| 0, 42, 1234         | '0|[1-9][0-9]*'        |
| Flotante | FLOAT_LITERAL  | 3.14, 0.001, 2.5e10 | `(0\.[0-9]+)|([1-9][0-9]*\.[0-9]+)([eE][+-]?[0-9]+)?`  |
| Cadena   | STRING_LITERAL | Hola, mundo!        | `([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))*\` |
| Caracter | CHAR_LITERAL   | a, '\n, 0x41        | `([\x20-\x7E]|\\([abefnrtv\\’\”]|0x[0-9a-fA-F]{2}))\`  |

- Entero: `0`, `42`, `1234`
- Flotante: `3.14`, `0.001`, `2.5e10`
- Cadena: `"Hola, mundo!"`
- Carácter: `'a'`, `'\n'`, `'0x41'`


### Identificadores

- Deben comenzar con una letra o guion bajo, seguidos de letras, dígitos o guiones bajos.

| Tipo          | Token | Funcion/Proposito  | Patrón Regex            |
|---------------|-------|--------------------|-------------------------|
| Identificador | ID    | Nombres de var/fin | `[A-Za-z_][A-Za-z0-9_]*`|

### Símbolos

| Simbolo | Token  | Función/Propósito    | Patrón Regex |
|---------|--------|----------------------|--------------|
| (       | LPAREN | Parentesis izquierdo | `\(`         |
| )       | RPAREN | Parentesis derecho   | `\)`         |
| {       | LBRACE | Llave izquierda      | `{`          |
| }       | RBRACE | Llave derecha        | `}`          |
| [       | LBRACK | Corchete izquierdo   | `\[`         |
| ]       | RBRACK | Corchete derecho     | `\]`         |
| ;       | SEMI   | Punto y coma         | `;`          |
| :       | COLON  | Dos puntos           | `:`          |
| ,       | COMMA  | Coma                 | `,`          |

- Paréntesis: `(`, `)`
- Corchetes: `[`, `]`
- Llaves: `{`, `}`
- Punto y coma: `;`
- Dos puntos: `:`
- Coma: `,`

## Documentación de Archivos


### b-minor.py
Es el archivo donde se ejecutara nuestro archivos de bminor

- Reconoce unicamente archivos con la extension .bminor
- Maneja los argumentos de línea de comandos usando `argparse`.
- Permite argumentos adicionales con el sistema `sys.exit`.
- Imprime mensajes con formato y color en consola `rich/print`.
- Funcion que ejecuta el analizador lexico sobre el codigo fuente `tokenize/lexer`.
  
- Soporta opciones:
  - Mostrar un mensaje de uso cuando el usuario no pasa argumentos validos o          cuando se requiere ayuda adicional `usage(exit_code=1)`, finaliza el programa     con el codigo de salida `exit_code`, 1=error.
      - Codigo de salida del sistema (0=correcto, 1=error)(Entero) `exit_code`
   
  - Configurar y procesar los argumentos de la CLI con `parse_args`
  - Define las opciones disponibles para el compilador
      - `-v`, `--version`: Muestra información de versión.
      - Archivo fuente B-Minor a compilar `filename`
      - `--scan`: Ejecuta el lexer y muestra los tokens.
      - `--dot`: Genera archivo DOT para el AST (no implementado).
      - `--sym`: Muestra la tabla de símbolos (no implementado).
  
  - `-h`, `--help`: Muestra el mensaje de ayuda.
  - Controla la ejecucion principal del compilador `main`, tambien valida que         pasen argumentos, abre el archivo fuente y ejecuta la fase correspondiente.
  - Si no se pasa ningun argumento  `len(sys.argv) ==1` se llama a  `usage()` y       se termina el programa
  - Se parsean los argumentos con  `parse_args()`
  - Lee el archivo fuente y pasa el contenido al lexer si se usa `--scan`.


### lexer.py

- Define la clase `Lexer` (hereda de `sly.Lexer`), especifica los tokens,           literales, caracteres ignorados y comentarios .
- Importamos `errors` desde `error`
- En `tokens` encontramos las palabras reservadas, operadores, literales e          identificadores
- `literals`
- Ignora espacios, tabulaciones y retornos de carro e ignora comentarios de una     linea `ignore` y `ignore_cppcomments`
- Gestiona lineas`ignore_newlines`
- Atributo de la clase Lexer, que mantiene el numero de linea actual en el          analisis`self.lineno`
- Valor del lexema `t.value`
- Tenemos el diccionario de palabras reservadas`Keywords`
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
  - `error`: Imprime errores en consola y los cuenta
- Variables globales: 
    - Instancia de console usada para imprimir mensajes formateados`console`
    - `_errors_detected`: Guarda el numero de erroes acumulados


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
Ejecuta el archivo "run_tests", y probara todos los archivos en la carpeta Test.


```powershell
python run_tests.py
```
Tambien puedes ver la tabla de del parser si le agregas el argumento --show-table
```powershell
python run_tests.py --show-table
```
---


## Dependencias

- Python 3.13.7
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

- Jhojan Felipe Sanchez Zapata
- Jonathan Muñoz Jimenez
- Valentina velasquez gil