from enum import Enum

CSS_CENTER = """    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
"""

APPJSON_CONST = """    "style": "v2",
    "componentFramework": "glass-easel",
    "sitemapLocation": "sitemap.json",
    "lazyCodeLoading": "requiredComponents"
"""

# 生成文件路径
PROJECT_DIR_NAME = "project"

JSON_CONST = """{
    "usingComponents": {}
}"""

Encoding = "utf-8"

class Theme(Enum):
    simple = 1
    fashion = 2
    retro = 3


class Function:
    @staticmethod
    def hasAblum():
        return """swiper-item > image {
    width: 100%;
}

"""

