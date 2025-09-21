# Generated from Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,3,2,24,8,2,1,2,3,2,
        27,8,2,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,1,10,31,0,
        10,1,0,0,0,2,12,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,31,1,0,0,0,10,
        11,3,2,1,0,11,1,1,0,0,0,12,13,5,12,0,0,13,18,3,4,2,0,14,15,5,12,
        0,0,15,17,3,4,2,0,16,14,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,
        1,0,0,0,19,3,1,0,0,0,20,18,1,0,0,0,21,23,3,6,3,0,22,24,3,8,4,0,23,
        22,1,0,0,0,23,24,1,0,0,0,24,27,1,0,0,0,25,27,3,8,4,0,26,21,1,0,0,
        0,26,25,1,0,0,0,27,5,1,0,0,0,28,29,7,0,0,0,29,30,5,11,0,0,30,7,1,
        0,0,0,31,32,5,13,0,0,32,9,1,0,0,0,3,18,23,26
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'child'", "'descendant'", "'descendant_or_self'", 
                     "'parent'", "'ancestor'", "'ancestor_or_self'", "'following'", 
                     "'following_sibling'", "'preceding'", "'preceding_sibling'", 
                     "'::/'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SLASH", "IDENTIFIER", "WS" ]

    RULE_query = 0
    RULE_pathExpr = 1
    RULE_step = 2
    RULE_axis = 3
    RULE_identifier = 4

    ruleNames =  [ "query", "pathExpr", "step", "axis", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    SLASH=12
    IDENTIFIER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathExpr(self):
            return self.getTypedRuleContext(GrammarParser.PathExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = GrammarParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.pathExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SLASH)
            else:
                return self.getToken(GrammarParser.SLASH, i)

        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StepContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StepContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_pathExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathExpr" ):
                listener.enterPathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathExpr" ):
                listener.exitPathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathExpr" ):
                return visitor.visitPathExpr(self)
            else:
                return visitor.visitChildren(self)




    def pathExpr(self):

        localctx = GrammarParser.PathExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pathExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(GrammarParser.SLASH)
            self.state = 13
            self.step()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 14
                self.match(GrammarParser.SLASH)
                self.state = 15
                self.step()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def axis(self):
            return self.getTypedRuleContext(GrammarParser.AxisContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStep" ):
                return visitor.visitStep(self)
            else:
                return visitor.visitChildren(self)




    def step(self):

        localctx = GrammarParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_step)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.axis()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 22
                    self.identifier()


                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_axis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxis" ):
                listener.enterAxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxis" ):
                listener.exitAxis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxis" ):
                return visitor.visitAxis(self)
            else:
                return visitor.visitChildren(self)




    def axis(self):

        localctx = GrammarParser.AxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_axis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 29
            self.match(GrammarParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = GrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





