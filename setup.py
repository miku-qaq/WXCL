from setuptools import setup, find_packages

setup(
    name="WXCL",  # 你的包的名字
    version="1.0.0",  # 包的版本
    packages=find_packages(),  # 自动发现所有包
    description="提供WXCL函数",  # 包的简短描述
    long_description=open('README.md', encoding='utf-8').read(), # 从 README.md 获取详细描述
    long_description_content_type="text/markdown",  # README 格式
    author="Kirito",  # 作者名字
    author_email="1013418280@qq.com",  # 作者邮箱
    url="https://github.com/miku-qaq/WXCL",  # 项目的主页
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 指定Python版本要求
)