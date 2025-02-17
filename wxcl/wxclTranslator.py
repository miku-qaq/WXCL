import logging

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from .wxclLexer import wxclLexer
from .wxclListener import wxclListener
from .wxclParser import wxclParser


# 通用错误监听器，适用于词法和语法分析
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error at line {line}, column {column}: {msg}"
        logging.error(error_message)  # 记录到日志
        raise RuntimeError(error_message)  # 直接抛出异常，终止解析


def translateWxcl(code: str) -> bool:


    # 设置日志配置
    logging.basicConfig(filename='translation_errors.log',
                        level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # 使用 ANTLR 的 InputStream 解析字符串
        input_stream = InputStream(code)

        # 创建词法分析器
        lexer = wxclLexer(input_stream)
        lexer.removeErrorListeners()  # 移除默认的错误监听器
        lexer.addErrorListener(MyErrorListener())  # 添加自定义错误监听器

        stream = CommonTokenStream(lexer)

        # 创建语法分析器
        parser = wxclParser(stream)
        parser.removeErrorListeners()  # 移除默认的错误监听器
        parser.addErrorListener(MyErrorListener())  # 添加自定义错误监听器

        # 开始解析
        tree = parser.project()  # 假设 'project' 是你的开始规则

        # 语法树遍历
        walker = ParseTreeWalker()
        listener = wxclListener()
        walker.walk(listener, tree)
        return True  # 如果解析成功，返回 True

    except (RuntimeError, Exception) as e:
        print(f"错误：{e}")
        return False
