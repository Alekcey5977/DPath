from antlr4 import *
from grammar_generated.GrammarLexer import GrammarLexer
from grammar_generated.GrammarParser import GrammarParser
from queryVisitor import QueryVisitor


def compiler_query(query, json_data):
    input_stream = InputStream(query)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.query()

    visitor = QueryVisitor(json_data)
    resalt = visitor.visit(tree)

    return resalt