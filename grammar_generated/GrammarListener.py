# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#query.
    def enterQuery(self, ctx:GrammarParser.QueryContext):
        pass

    # Exit a parse tree produced by GrammarParser#query.
    def exitQuery(self, ctx:GrammarParser.QueryContext):
        pass


    # Enter a parse tree produced by GrammarParser#pathExpr.
    def enterPathExpr(self, ctx:GrammarParser.PathExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#pathExpr.
    def exitPathExpr(self, ctx:GrammarParser.PathExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#step.
    def enterStep(self, ctx:GrammarParser.StepContext):
        pass

    # Exit a parse tree produced by GrammarParser#step.
    def exitStep(self, ctx:GrammarParser.StepContext):
        pass


    # Enter a parse tree produced by GrammarParser#axis.
    def enterAxis(self, ctx:GrammarParser.AxisContext):
        pass

    # Exit a parse tree produced by GrammarParser#axis.
    def exitAxis(self, ctx:GrammarParser.AxisContext):
        pass


    # Enter a parse tree produced by GrammarParser#identifier.
    def enterIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#identifier.
    def exitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        pass



del GrammarParser