import os
import sys

from wxcl.wxclTranslator import translateWxcl

if __name__ == '__main__':
    """
        解析 wxcl 代码字符串。

        参数:
            code (str): 需要解析的 wxcl 代码

        返回:
            bool: 解析成功返回 True，否则返回 False
    """

    # 获取 Driver 所在的目录
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # 强制修改当前工作目录（cwd）
    os.chdir(base_dir)

    # 只从 input.txt 读取代码
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            wxcl_code = f.read()
    except FileNotFoundError:
        print("错误：找不到 input.txt 文件")
        sys.exit(1)

    # 调用翻译函数
    if translateWxcl(wxcl_code):
        print("翻译成功！")
    else:
        print("翻译失败！请查看日志文件。")