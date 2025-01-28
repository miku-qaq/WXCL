# -*- coding: gbk -*-
import sys
from antlr4 import *

from gen.wxclListener import wxclListener
from wxclLexer import wxclLexer
from wxclParser import wxclParser


def main(argv):
    input_stream = FileStream(argv[1], encoding='gbk')
    lexer = wxclLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = wxclParser(stream)
    tree = parser.project()
    walker = ParseTreeWalker()
    listener = wxclListener()
    walker.walk(listener, tree)
    print("miku觉得很ok！")


if __name__ == '__main__':
    main(sys.argv)
