# Lab1_Compiladores

## Descripción de los archivos clave

### `program/MiniLang.g4`

* **Header**: `grammar MiniLang;` define el nombre.
* **Reglas del parser** :

  * `prog: stat+ ;`  Regla de inicio.
  * `stat: expr NEWLINE #printExpr | ID '=' expr NEWLINE #assign | NEWLINE #blank ;`
  * `expr: expr ('*'|'/') expr #MulDiv | expr ('+'|'-') expr #AddSub | INT #int | ID #id | '(' expr ')' #parens ;`
* **Lexer rules** (UPPERCASE):

  * `MUL : '*' ;`, `DIV : '/' ;`, `ADD : '+' ;`, `SUB : '-' ;`
  * `ID  : [a-zA-Z]+ ;` identifica variables.
  * `INT : [0-9]+ ;` reconoce números.
  * `NEWLINE: '\r'? '\n' ;` fin de sentencia.
  * `WS  : [ \t]+ -> skip ;` ignora espacios.


### `program/Driver.py`

```python
from antlr4 import FileStream, CommonTokenStream
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

def main(argv):
    input_stream = FileStream(argv[1]) #lee el archivo de entrada
    lexer = MiniLangLexer(input_stream) #crea el lexer
    stream = CommonTokenStream(lexer) #bufferiza los tokens
    parser = MiniLangParser(stream) #crea el parser
    tree = parser.prog() # Inicia en 'prog'

if __name__ == '__main__':
    main(sys.argv)
```


### `program_test.txt`

Ejemplo de programa en MiniLang:

```
5 * 5
a = 4
b = 6
c = a + b
```



