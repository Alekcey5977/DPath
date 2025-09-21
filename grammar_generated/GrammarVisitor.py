# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#query.
    def visitQuery(self, ctx:GrammarParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pathExpr.
    def visitPathExpr(self, ctx:GrammarParser.PathExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#step.
    def visitStep(self, ctx:GrammarParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#axis.
    def visitAxis(self, ctx:GrammarParser.AxisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)



del GrammarParser