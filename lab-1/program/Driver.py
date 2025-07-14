import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

def main(argv):
    input_stream = FileStream(argv[1]) #lee el archivo de entrada
    lexer = MiniLangLexer(input_stream) #crea el lexer
    stream = CommonTokenStream(lexer) #bufferiza los tokens
    parser = MiniLangParser(stream) #crea el parser
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

if __name__ == '__main__':
    main(sys.argv)