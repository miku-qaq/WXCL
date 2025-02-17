import json
import os
import re

from .tool import *


def format_wxml(wxml_content):
    """格式化 WXML 内容，添加合适的缩进并整理标签。"""
    indent_level = 0
    formatted_content = []

    # 通过换行分割 WXML 内容
    lines = wxml_content.splitlines()

    for line in lines:
        # 删除每行的前后空格
        line = line.strip()

        # 跳过空行
        if not line:
            continue

        # 如果是闭合标签（</tag>），减少缩进
        if re.fullmatch(r'</[^>]+>', line):
            indent_level -= 1

        # 添加缩进
        formatted_content.append('\t' * indent_level + line)

        # 如果是开标签（<tag> 或 <tag />），增加缩进
        if re.fullmatch(r'<[^/][^>]*[^/]>', line):  # 普通开始标签
            indent_level += 1

    return '\n'.join(formatted_content)


def format_wxss(content):
    """格式化 WXSS (CSS) 文件"""
    from cssbeautifier import beautify
    return beautify(content, {"indent_size": 2})  # 2 空格缩进


def format_js(content):
    """格式化 JavaScript 代码"""
    import jsbeautifier
    return jsbeautifier.beautify(content, {"indent_size": 2})  # 2 空格缩进


def format_json(content):
    """格式化 JSON 文件"""
    try:
        data = json.loads(content)  # 解析 JSON
        return json.dumps(data, indent=2, ensure_ascii=False)  # 2 空格缩进
    except json.JSONDecodeError:
        return content  # 解析失败，返回原内容


def format_file(file_path):
    """根据文件类型格式化文件"""
    _, ext = os.path.splitext(file_path)
    with open(file_path, "r", encoding=Encoding) as f:
        content = f.read()

    if ext == ".wxml":
        formatted_content = format_wxml(content)
    elif ext == ".wxss":
        formatted_content = format_wxss(content)
    elif ext == ".js":
        formatted_content = format_js(content)
    elif ext == ".json":
        formatted_content = format_json(content)
    else:
        print(f"跳过 {file_path}（不支持的格式）")
        return

    with open(file_path, "w", encoding=Encoding) as f:
        f.write(formatted_content)
    print(f"格式化完成: {file_path}")


def format_directory(directory):
    """格式化指定目录下的所有 WXML、WXSS、JS、JSON 文件"""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".wxml", ".wxss", ".js", ".json")):
                format_file(os.path.join(root, file))
